## CharacterPalette

> `/System/Library/Input Methods/CharacterPalette.app/Contents/MacOS/CharacterPalette`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-424.0.0.0.0
-  __TEXT.__text: 0x1ea5c
+424.1.1.0.0
+  __TEXT.__text: 0x1ec48
   __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_stubs: 0x6b40
-  __TEXT.__objc_methlist: 0x300c
+  __TEXT.__objc_stubs: 0x6ba0
+  __TEXT.__objc_methlist: 0x301c
   __TEXT.__cstring: 0x19d9
-  __TEXT.__objc_methname: 0x8d86
+  __TEXT.__const: 0x568
+  __TEXT.__objc_methname: 0x8de9
+  __TEXT.__oslogstring: 0x7e0
   __TEXT.__objc_classname: 0x686
   __TEXT.__objc_methtype: 0x2351
-  __TEXT.__const: 0x560
   __TEXT.__ustring: 0xa
-  __TEXT.__oslogstring: 0x67c
   __TEXT.__gcc_except_tab: 0xd4
   __TEXT.__unwind_info: 0xac8
   __DATA_CONST.__const: 0x7f8

   __DATA_CONST.__got: 0x3e0
   __DATA_CONST.__auth_ptr: 0x68
   __DATA.__objc_const: 0x8be8
-  __DATA.__objc_selrefs: 0x2600
+  __DATA.__objc_selrefs: 0x2618
   __DATA.__objc_ivar: 0x350
   __DATA.__objc_data: 0x1360
   __DATA.__data: 0x638

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 792
+  Functions: 793
   Symbols:   274
-  CStrings:  2286
+  CStrings:  2293
 
CStrings:
+ "CharacterPalette popover did close, entering standby"
+ "CharacterPalette resigning from app, process state %{public}@, terminating immediately: %d"
+ "CharacterPalette setValue: %@ client: %@ process state: %{public}@ visible popover: %d"
+ "CharacterPalette was dismissed by outside input moments ago, so treat this invocation as a toggle off"
+ "CharacterPalette window %{public}@ will close, entering standby"
+ "_shouldToggleOffRatherThanActivate"
+ "clearDismissalByOutsideInput"
+ "wasRecentlyDismissedByOutsideInput"
- "CharacterPalette setValue: %@ client: %@"
```
