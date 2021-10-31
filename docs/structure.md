#Structure - General Idea

Kookaburra is a "batteries included" forum package that can fit most needs.
Its two primary use cases are:
- as a standalone forum
- as a plugable forum to an existing django (or wagtail) site.

## Preliminary ideas:

Multiple post types deviate from a "BasePost" (discussed later)

a "Post" object is analogous to a thread/OP in forum software
a Post then receives comments from others.

The Post becomes the focus point; any "shared" items commented with ( images, files, etc) get bubbled up to become part of the Post.

This is configurable when making a post; for instance:
```py
Post(
    "Post your cool recipes here",
    bubble_files = True,
    bubble_links=True,
    bubble_images=False
)
```
Would make a Post that would have the subject / message asking people to post cool recipes, and would bubble those files (assumping they're shared as pdf or links, etc) to the top of the post, so that people don't have to scroll through the whole post (and pages of pages of comments) to find all the recipes. It would be presented in the OP as a "attached files" tab or otherwise.

Images would not be bubbled, and so they would be as part of the comment. This could be for people who wanted to share a photo of what they cooked. The link from the file in the OP would have a link to the originating comment.

Something like a "exec meeting minutes" post (which is updated each month with the meeting minutes for everyone to see) would similarly aggregate files.

Images could be presented in a "gallery" type of post, or perhaps if they are showing progression, they would be left "in-time" in the comments, which would show why the aggregation would not work in that situation (the images belong more to the stories, for instance.


BasePost has the following properties:

### BasePost

- `is_followable`, `followed_by` users.
    - this allows users of the forum to "follow" a post, whenever the post gets updated or commented on.
      the following users would be able to "see" this in their recent activity that they're interested in.

- `Is stickied` 
    for when the post is "stickied" to the top of it's channel that it is posted in.

- `Is Locked`
    unable to be commented on (TODO: something about "unable to be edited")

- `Is commentable` 
    unable to be commented on

- Moderators only - only moderators of the group can add resources.

relation to other models
    Comments
    Followers
    Group - which group is it a part of

### LinksPost
LinksPost becomes an agregator of links (think hackernews)
where Links get bubbled to be front and centre of a post.
(this will come in handy when people want to make "Useful links to help with X" posts, which can be added to, or comments from other parts of the forum could also be copied to)

### FilesPost
A Files-Focused post that aggregates files, which could be used for archival purposes. such as keeping a record of meeting minutes.

### TODOPost
A singular todo item. This could be used for items such as "things that need fixing by the maintenance team" in an eco-village setting. The point of this would be that it would be presented in such a way that all the comments and information would be linked into this post, which can then be marked Done or Assigned to members or similar.

### EventPost
A post about an Event. Attached to a datetime, which forms a bit of a calandar. Could also be set up to be recurring and markng people for attendance.

### PollPost
A general Poll, much like a regular Post but with a fat bar graph in the middle of it ( or radio buttons if you have not yet voted)

### DiscussionPost
A general regular post, someone writres something, someone responds with something.

--------------------------------------

## Page / Section / Room / Channel 

each section of the forum would be able to contain posts related to that group. with the addition of a "general" page, that would be shared across all memebers. EAch post into each sub-comittee "page" would would then have the option to link to "general" page as well. 

For instance, if a "Social group" wants to post an Event, they could post it on their group, but link it with the "general" page as well. so that even people who are not following the social group ( or are not members of the social group) get the notification as well.

Each page can turn on/off the types of post that they accept. (cross linking does not (yet) be affected by this)

Pages have the option of:
- showing posts in a grid manner (to be a smorgasboard of information, like a general information page)
- showing posts in a list manner (traditional forum)
- showing posts in a calendar manner (optionally filtering only for events)
---
any misc posts that are ALLOWED to be posted on the page but FILTERED by the view will be present in the List view.

Each option of List / Grid / Cal would be togglable on/off, set filters for, [Duplicated by name?] as well as set primary view.

Each page would also have it's own front matter to have a shiny face ( like an about page)

For instance:
Foodbowl Section
- main about page would have a list view.
- optional calandar view (tab)
- optonal [list view] "How To guides" (tab) filtering normal posts with #how
- optional [grid view]"Plant ID" (tab) filtering Normal posts with #plantid
- another tab being specific link to specific post.
- ALLPOSTS

Social Section
- main about page would have a cal view.
- optional [list view] "Discsussion" (tab) filtering PollPosts
- ALLPOSTS

Exec Section
- Grid view about page with legal and guides.
- Link to specific files in tabs.
- ALLPOSTS

Maintenance Section
- Main View list (concise) filtered by (active)
- Secondary view files list
- grid view how to guides 
- cal view filtering for events and TODO.
