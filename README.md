# FlaskDemo
## Purpose
This is a simple application for showcasing Flask basics like routes between backend and frontend.
Using a very generic example dataset (`tips` from the seaborn library), I built a two-page application.

|    |   total_bill |   tip | sex    | smoker   | day   | time   |   size |
|---:|-------------:|------:|:-------|:---------|:------|:-------|-------:|
|  0 |        16.99 |  1.01 | Female | No       | Sun   | Dinner |      2 |
|  1 |        10.34 |  1.66 | Male   | No       | Sun   | Dinner |      3 |
|  2 |        21.01 |  3.5  | Male   | No       | Sun   | Dinner |      3 |
|  3 |        23.68 |  3.31 | Male   | No       | Sun   | Dinner |      2 |
|  4 |        24.59 |  3.61 | Female | No       | Sun   | Dinner |      4 |

## Structure
### Page 1
On the first page one can filter the dataset by a minimum `tip`-value entered in a textbox. The results of the filtering are shown after clicking the submit button.

### Page 2
Page 2 acts as an input form to a very simple Linear Regression model trained on the data. As the model is a vanilla Regression Model without optimization or regularization it performs quite poorly. Note however, that the purpose of the project is to showcase Flask, not predictive modelling.

## Technical Explanation
* on submit, the form sends a POST request to `/`
* all form elements (only one in this case) are read from the `request` object
    * this is specific to forms, otherwise the request could have been jsonified
* the `app.py` performs filtering and renders the landingpage template again, this time passing the filtered html-version of the dataframe as a parameter
* the parameter in the template renders due to the **jinja2** syntax in the html