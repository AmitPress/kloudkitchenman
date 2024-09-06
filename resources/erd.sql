// auth amit malaker
// warning this is not an sql file 
// kindly goto dbdiagram.io and copy paste this to hhave a gui view
// every table below will have created_at and updated_at fields


Table Resturant{
  id integer [pk]
  name varchar
  location varchar
  opens_at timestamp
  closes_at timestamp 
  owner integer [ref: > Owner.id]
}

Table Owner{
  id integer [pk]
  name varchar
  email varchar
  password varchar
  address varchar 

  dob timestamp
  resturant integer [ref: < Resturant.id]
}

Table Employee{
  id integer [pk]
  name varchar
  email varchar
  password varchar
  address varchar 

  resturant integer [ref: > Resturant.id]
}

Table Customer{
  id integer [pk]
  name varchar
  email varchar
  password varchar
  address varchar 

  order integer [ref: < Order.id]
  discount_coupon integer [ref: <> Coupon.id]
  completed_orders integer
}

Table Order{
  id integer [pk]
  items integer [ref: < Item.id]
  state tuple(inprocess, placed, completed)
  customer integer [ref: > Customer.id]
  applied_coupon integer [ref: - Coupon.id]
  total_price double
  dicounted_price double
}
Table Coupon{
  id integer [pk]
  name varchar 
  occasion varchar
  discount_percentage double
  available boolean
}
Table Item{
  id integer [pk]
  name varchar
  description varchar
  price double 
  category integer [ref: <> Category.id]
  discount double
  modifier integer [ref: < Modifier.id]
  available boolean
}
Table Category{
  id integer [pk]
  type varchar 
  name varchar 
  item integer [ref: <> Item.id]
  discount double
  available boolean
}

Table Modifier{
  id integer 
  type varchar 
  name varchar 
  price double 
  discount double 
  item integer [ref: > Item.id]
  available boolean
}
Table Card{
  type tuple(debit, credit)
  number integer 
  cvv integer 
  expiration varchar 
  postal_code integer
  belongs_to integer [ref: - Customer.id]
}