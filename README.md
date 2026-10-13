# Coffee Shop Staffing Dashboard

## Team 9 

## Dataset

This project uses the Coffee Shop Sales dataset from Kaggle.

Dataset link: https://www.kaggle.com/datasets/ahmedabbas757/coffee-sales

The dataset contains sales records from a fictional coffee shop business. Each row represents one product sales record, including the transaction date, transaction time, store location, product category, quantity sold, and unit price.

The data period is January 1, 2023 to June 30, 2023. The dataset is a fixed Kaggle snapshot, so it does not update automatically.

## Decision-Maker

The dashboard is designed for a coffee shop store manager.

It is not designed for everyone in the company. A store manager needs a simple operational view that helps with staffing decisions by hour and by store location.

## Business Decision

The dashboard supports staffing decisions.

If a store manager sees that certain hours have consistently high sales record volume, they will schedule more staff during those hours. If some hours have low sales record volume, they may schedule fewer staff to control labor costs.

The main decision sentence is:

If the store manager sees high hourly sales demand on this dashboard, they will add staff to those hours in the weekly schedule.

## Why a Dashboard?

A dashboard is useful because staffing is a repeated operational decision. Store managers need to review demand patterns regularly before creating schedules.

A one-time report would not be enough because sales demand can differ by store, date range, and product category. A weekly email would be less flexible because the manager could not easily filter the data. An alert alone would also not be enough because the manager needs to compare demand across many hours, not only react to one extreme number.

## Dashboard Design

The dashboard includes three headline metrics:

1. Total Sales
2. Sales Records
3. Average Records per Open Hour

These metrics appear at the top because the manager should understand the overall demand level within a few seconds of opening the page.

The dashboard includes two supporting charts:

1. Hourly Demand
2. Sales by Product Category

The hourly demand chart is the most important chart because staffing decisions are made by time of day. The product category chart helps the manager understand what types of products drive sales demand.

The dashboard includes filters for:

1. Store Location
2. Product Category
3. Date Range

These filters are useful because a store manager may need to focus on one store, one time period, or one part of the business.

## What We Chose Not to Show

We chose not to show customer-level analysis because the dataset does not include customer IDs. It would be misleading to discuss customer behavior without customer information.

We also chose not to show profit or margin because the dataset does not include cost data. The dashboard shows sales revenue, not profit.

## Possible Data Limitations

The dataset is from a fictional coffee shop business, so it should be treated as simulated business data rather than evidence from a real coffee chain.

Each row is a product sales record, not necessarily a complete customer order. Because of this, the dashboard uses the term "sales records" instead of "customers."

The dataset only covers January 1, 2023 to June 30, 2023. It does not show a full year, so the dashboard should not be used to analyze full-year seasonality.

The CSV does not include labor cost, staffing levels, inventory, customer wait time, or customer satisfaction. This means the dashboard can suggest when demand is high, but it cannot directly prove the perfect number of employees needed.

## Refresh Frequency

In a real coffee shop, sales data should refresh nightly from the point-of-sale system.

The store manager should review the dashboard weekly before creating staff schedules. Real-time refresh is not necessary because staff schedules are usually planned in advance.

One metric that should trigger action is average sales records per open hour. If a specific hour is much higher than the store's normal hourly pattern for several weeks, the manager should consider adding staff during that hour.

Stale data could lead to poor staffing decisions. If the dashboard is a week out of date, the manager might miss a recent increase in demand and schedule too few employees during busy hours.