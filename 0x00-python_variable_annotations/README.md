# 0x00. Python - Variable Annotations

## Description
This project covers Python variable annotations, focusing on type hints and how to validate them using `mypy`. You will practice applying type annotations, understanding duck typing, and making code more readable and maintainable.

## Learning Objectives
By the end of this project, you will:
- Know how to use Python's type annotations.
- Apply duck typing concepts.
- Validate code with `mypy`.

## Requirements
- Python version: 3.7
- Ubuntu 18.04 LTS
- All scripts must be executable.
- Use `pycodestyle` for style consistency.
- Code must be well-documented.

## Project Structure

### Tasks

1. **0-add.py**  
   A function `add` that takes two floats and returns their sum.

2. **1-concat.py**  
   A function `concat` that concatenates two strings.

3. **2-floor.py**  
   A function `floor` that returns the floor value of a float.

4. **3-to_str.py**  
   A function `to_str` that converts a float to a string.

5. **4-define_variables.py**  
   Annotate variables with types: `a`, `pi`, `i_understand_annotations`, and `school`.

6. **5-sum_list.py**  
   A function `sum_list` that sums a list of floats.

7. **6-sum_mixed_list.py**  
   A function `sum_mixed_list` that sums a list of integers and floats.

8. **7-to_kv.py**  
   A function `to_kv` that returns a tuple with a string and the square of an integer or float.

9. **8-make_multiplier.py**  
   A function `make_multiplier` that returns a function multiplying a float by a given multiplier.

10. **9-element_length.py**  
    Annotate a function `element_length` that returns a list of tuples containing the element and its length.

11. **101-safely_get_value.py**  
    Add type annotations to the `safely_get_value` function, which retrieves a value from a dictionary if the key exists, or returns a default value.
    ```python
    from typing import Mapping, Any, Union, TypeVar

    T = TypeVar('T')

    def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
        if key in dct:
            return dct[key]
        else:
            return default
    ```

12. **102-type_checking.py**  
    Validate the following code with `mypy`, apply corrections, and annotate types:
    ```python
    from typing import List, Tuple

    def zoom_array(lst: Tuple, factor: int = 2) -> List:
        zoomed_in: List = [
            item for item in lst
            for i in range(factor)
        ]
        return zoomed_in

    array = [12, 72, 91]
    zoom_2x = zoom_array(tuple(array))
    zoom_3x = zoom_array(tuple(array), 3)
    ```

## Usage
Run each script using:
```bash
./<filename>.py

