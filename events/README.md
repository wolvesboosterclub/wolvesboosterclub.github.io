This directory is special and should never be empty (at least this README should always be included).

The directory is designed to contain JSON files detailing events that are happening/have happened in coordination with the Wolves Booster Club. Each file has a specific format (really just specific JSON fields) and failing to edit/create these files will result in errors both here in GithUb and in the website (causes events to disappear from the site).

Below is all of the fields the JSON may contain to be used by the website and a sample event json file is shown after.

| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| title                 | A simple title that shows up on the main page and at the top of the event view.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| start_datetime        | The date and time the event starts at. The format is the all-supported JS format: YYYY-MM-DDTHH:MM. For example, March 14th of 2024, at 6:32PM would be 2024-03-14T18:32. Note, the T character between the date and the time is required. You can also add tiemzone offsets. EST is -05:00 and EDT is -04:00. An EDT datetime would then look like 2024-03-14T18:32-04:00; adding timezone information is very important! If you want an event to be "all day", just use the year month and day with no time, i.e. 2024-07-14. Refer to https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_time_string_format. |
| end_datetime          | (Optional) The date and time the event ends at. This may be the same day and/or time as start_datetime but must not be before. This field has the exact same format as start_datetime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| short_description     | This brief description of the event is what is shown on the homepage event listing and on event listings page. Make it short and sweet, extra text may get cut off.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| description           | This is where the all the details will be stored (save the date/time). Here is where you describe the event in detail, location, prices, links to signup, etc. This field cannot contain newlines in the traditional "press enter" way; JSON does not support that. Thus, the contents of this field will either need to be one long string of text that will be rendered as one paragraph or it will need to have HTML embeeded to force line breaks and styling.                                                                                                                                                                                      |
| manning               | (Optional) This is an object field. It will contain either one or two fields. If the field is used, it must contain the child field `attending` to show how many people have signed up to users. If may also contain the field `needed` to show that the event needs a certain number of people. Refere to the examples below.                                                                                                                                                                                                                                                                                                                          |
| linked_gallery_images | (Optional) This field is a JSON list that contains filenames of gallery images to show on the event page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| linked_news           | (Optional) This field is a JSON list of news filenames to link on the event page so users can see recent news posted relating to the event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

Minimal example (fictitous):

```
{
    "title": "A Simple Event",
    "start_datetime": "2024-07-14T09:00:00",
    "short_description": "It really is that simple!",
    "description": "A simple event for the simple things! Come out and enjoy.<br/>Because this event is so simple, do we really need all this description? I think not! Just come out to the <a href=\"https://maps.app.goo.gl/uPADauLM4gmkpEXt6\">Location</a>"
}
```

Full example (also ficticious, the filenames/references don't exist):

```
{
    "title": "The Go-Getter Event",
    "start_datetime": "2024-11-23T15:30:00",
    "end_datetime": "2023-11-23T21:00:00",
    "short_description": "If you go all out, this event is for you!",
    "description": "We've never heard of minimalism and we aren't about to learn it now!<br/>We need 200 wonderous folks to come out and party as hard as they can! There will be baloons, confettie, confettie <b>GUNS</b>.<br/>Oh, and did we mention it would hosted at the Confettie Capital of the WORLD? Yeah. That's right. Let's do this.",
    "manning": {
        "needed": 200,
        "attending": 126
    },
    "linked_gallery_images": [
        "confettie_capital.png"
    ],
    "linked_news": [
        "confettie_amount_increase.json"
    ]
}
```
