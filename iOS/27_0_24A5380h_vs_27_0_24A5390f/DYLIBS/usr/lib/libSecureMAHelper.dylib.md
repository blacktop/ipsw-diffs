## libSecureMAHelper.dylib

> `/usr/lib/libSecureMAHelper.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-2215.0.13.0.0
-  __TEXT.__text: 0x1e548
+2215.0.16.0.0
+  __TEXT.__text: 0x1e540
   __TEXT.__objc_methlist: 0x57c
   __TEXT.__const: 0x510
   __TEXT.__cstring: 0x6e91
-  __TEXT.__oslogstring: 0x2e15
+  __TEXT.__oslogstring: 0x2e25
   __TEXT.__gcc_except_tab: 0x9a8
   __TEXT.__unwind_info: 0x538
   __TEXT.__objc_stubs: 0x0
Functions:
~ _getPlistDictionary : 516 -> 508
CStrings:
+ "[ERROR] %{public}s: Extracted object for key %{public}@ is invalid/not a dictionary"
+ "[ERROR] %{public}s: Unable to extract plist object for key %{public}@ from dict"
- "%{public}s: Extracted object for key %{public}@ is invalid/not a dictionary"
- "%{public}s: Unable to extract plist object for key %{public}@ from dict"
```
