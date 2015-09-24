# Description

The file is going to basically be a mapping of key/value pairs.

The only current valid key is a raw string beginning with an alphabetic character 
followed by any number of underscores and alphanumeric characters. Key are to be 
case insensitive.

The key may be followed by any ammount of the whitespace characters, space, and tab, 
the a colon character.

The colon may have whitespace after it in a similer fasion as the key.

The final token is the value. The value is going to be any of the datatypes descibed 
in the section, [Value Datatypes](#value_datatypes).

The final syntax rule is comments. Anytime a `#` character appears, the rest of 
that line is to be interpreted as a comment. The only exception is when it is found
within a string token. Ex: `some_key: "# I'm not a comment" # I'm a comment`

## Value Datatypes<a name="value_datatypes"></a>

* **Numerics**
    * **Integer** -
        Any whole number. Ex: `-420`, `326`, `0`.
    * **Floating Points** -
        Any floating point value. Ex: `-2.4`, `1995.98754836`, `0.0`.
        Alternative syntax. Ex: `5.` == `5.0`, `.8` == `0.8`.
* **Strings** -
    Any value contained with in two `'` characters, or two `"` characters. All python 
    string escapes should be valid within our style strings. Ex: `'I\'m a single string still.'`, 
    `"\"I'm a single string still.\" --Last Guy"`
* **Boolean** -
    The strings `true` and `false`.
* **Null** -
    The string `null` denotes that the data is null.

### Potential Data Types

* **Arrays** -
    `key[]: [1, 2, 3]`
    or
    ```
    key[0]: 1
    key[1]: 2
    key[2]: 3
    ```

* **Stored Object Refrences**

## Examples 

    key: 'value' #comment
    apPle                :42
    no_me:    null
    is_mean: true
    is_FRIENDLY  : false
