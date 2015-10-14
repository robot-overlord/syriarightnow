# Syria Right Now
A warning system for civilians amidst the Syrian Civil War

# Project Status

| Branch         | Integration | Code Quality | Test Coverage |
|----------------|-------------|--------------|---------------|
| Master         | `not configured` | `not configured` | `not configured` |

## Up Next
- [ ] Tests
- [ ] Pull data from Facebook
- [ ] Pull data from YouTube
- [ ] Extract location data (or use known location associated with account)
- [ ] Live map of Syria
- [ ] Add symbols based on keywords

## Installation
- Ensure you have Python 2.7.9 installed
- Ensure you have Pip installed
- Ensure you have VirtualEnv installed
- Clone the repository
 ```
 git clone git@github.com:robot-overlord/syriarightnow.git
 ```
- Change into project root directory
 ```
 cd syriarightnow
 ```
- Load up Virtual Env
```
source venv/bin/activate
```
- Copy `.env.example` and rename as `.env` and replace placeholder text with correct keys
- Start the Application
 ```
 foreman start
 ```

## Emoji tags for commits, PRs and comments
| Platform             | Symbol           | Markdown           |
|----------------------|------------------|-------------------:|
| Linux/Android        | :penguin:        | `:penguin:`        |
| OS X / iOS           | :apple:          | `:apple:`          |
| Windows / WindowsPhone | :checkered_flag: | `:checkered_flag:` |
| BlackBerry           | :grapes:         | `:grapes:`         |

| Device Size          | Symbol           | Markdown           |
|----------------------|------------------|-------------------:|
| Smartphone           | :iphone:         | `:iphone:`         |
| Tablet               | :scroll:         | `:scroll`          |
| Desktop              | :computer:       | `:computer`        |

| Meaning                         | Symbol              | Markdown              |
|---------------------------------|---------------------|----------------------:|
| Idea                            | :bulb:              | `:bulb:`              |
| Approval                        | :+1:                | `:+1:`                |
| Improving code format/structure | :art:               | `:art:`               |
| Improving performance           | :racehorse:         | `:racehorse:`         |
| Plugging memory leaks           | :non-potable_water: | `:non-potable_water:` |
| Writing docs                    | :memo:              | `:memo:`              |
| Bug Fix                         | :bug:               | `:bug:`               |
| Removing code or files          | :fire:              | `:fire:`              |
| Fixing CI build                 | :green_heart:       | `:green_heart:`       |
| Adding tests                    | :white_check_mark:  | `:white_check_mark:`  |
| Security fix                    | :lock:              | `:lock:`              |
| Upgrading dependencies          | :arrow_up:          | `:arrow_up:`          |
| Downgrading dependencies        | :arrow_down:        | `:arrow_down:`        |
| Fix linter warning              | :shirt:             | `:shirt:`             |

# Style Guides
| Language        | Guide                                   |
|-----------------|----------------------------------------:|
| Python          | [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) |
| Sass (`*.sass`) | Essentially enforced by the syntax      |
| Sass (`*.scss`) | [Official Sass Styleguide](http://sass-lang.com/styleguide) |
| JavaScript      | [AirBnb](https://github.com/airbnb/javascript) |
| Git Commits     | [GitHub Guide](https://github.com/blog/926-shiny-new-commit-styles) |
| Pull Requests   | [Pull Requests](https://github.com/blog/1943-how-to-write-the-perfect-pull-request) |
