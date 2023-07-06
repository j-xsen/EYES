
# EYES

A project which ventures into creating digital art through the use of [Panda3D](https://awesomeopensource.com/project/elangosundar/awesome-README-templates).

Generates GIFs from screenshots taken of a collage of EYES staring.
## Installation

Clone the project

```bash
  git clone https://github.com/j-xsen/EYES.git
```

Install the requirements

```bash
  pip install -r requirements.txt
```
## Config

Variables are set for the program in the `config/` folder

- `Config.prc` contains mostly integer values
- `Config.py` imports the `Config.prc` values and defines a couple lists

### Variables

<details>
<summary>
<h4>Config.prc</h4>
</summary>

|name|default|description|
|--|--|--|
|`fullscreen`|#f|Toggles fullscreen|
|`win-size`|2048 2048|Output resolution|
||
|`min-cubes`|300|Minimum number of cubes to create|
|`max-cubes`|400|Maximum number of cubes to create|
|`min-eyes`|256|Minimum number of eyes to create|
|`max-eyes`|1024|Maximum number of eyes to create|
||
|`rotate-time`|3|Duration of animation in seconds|
|`fps`|10|Screenshots for Panda3D to take per second|
|`gifs-to-make`|50|Number of gifs to render|
||
|`number-eye-variants`|4|Number of eye variants|
||
|`min-pos-x`|-1000|Minimum X position to create Objects|
|`max-pos-x`|1000|Maximum X position to create Objects|
|`min-pos-y`|1000|Minimum Y position to create Objects|
|`max-pos-y`|5000|Maximum Y position to create Objects|
|`min-pos-z`|-1000|Minimum Z position to create Objects|
|`max-pos-z`|1000|Maximum Z position to create Objects|
|`min-hpr-x`|-100|Minimum H position to create Objects|
|`max-hpr-x`|300|Maximum H position to create Objects|
|`min-hpr-y`|-25|Minimum P position to create Objects|
|`max-hpr-y`|25|Maximum P position to create Objects|
||
|`default-directnotify-level`|warning|A Panda3D debug option|
|`notify-level`|warning|Base debug output level|
|`notify-level-jxndbg`|debug|Debug output level for my code|


</details>

<details>
<summary>
<h4>Config.py</h4>
</summary>

|name|description|usage|
|--|--|--|
|`color_groups`|A dictionary of ColorGroups, sorted by name|Used to add more color diversity by having one string be equal to numerous colors|
|`maps`|An array of Maps consisting of MapNodes|Defines the boundaries for the program to follow, color-wise|


</details>



## Run

Run run.py

```bash
python run.py
```
## Example

![Example Screenshot](https://raw.githubusercontent.com/j-xsen/EYES/main/example.jpg)

