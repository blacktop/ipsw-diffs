## WorkoutHealthPlugin

> `/System/Library/Health/Plugins/WorkoutHealthPlugin.bundle/WorkoutHealthPlugin`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2027.2.25.0.0
-  __TEXT.__text: 0x9b94
+2027.2.34.0.0
+  __TEXT.__text: 0x9ef4
   __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_stubs: 0x1920
-  __TEXT.__objc_methlist: 0xce4
-  __TEXT.__cstring: 0x21cd
-  __TEXT.__objc_methname: 0x2365
+  __TEXT.__objc_stubs: 0x1960
+  __TEXT.__objc_methlist: 0xd04
+  __TEXT.__cstring: 0x21f9
+  __TEXT.__objc_methname: 0x23d1
   __TEXT.__objc_classname: 0x1fb
-  __TEXT.__objc_methtype: 0x953
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__oslogstring: 0x1130
-  __TEXT.__unwind_info: 0x350
-  __DATA_CONST.__const: 0xb30
-  __DATA_CONST.__cfstring: 0x8c0
+  __TEXT.__objc_methtype: 0x970
+  __TEXT.__const: 0x80
+  __TEXT.__gcc_except_tab: 0x280
+  __TEXT.__oslogstring: 0x1189
+  __TEXT.__unwind_info: 0x368
+  __DATA_CONST.__const: 0xb58
+  __DATA_CONST.__cfstring: 0x8e0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__auth_got: 0x2c0
-  __DATA_CONST.__got: 0x1c0
-  __DATA.__objc_const: 0xdf0
-  __DATA.__objc_selrefs: 0x9d8
+  __DATA_CONST.__got: 0x1c8
+  __DATA.__objc_const: 0xdf8
+  __DATA.__objc_selrefs: 0x9f0
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x420

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 213
-  Symbols:   751
-  CStrings:  593
+  Functions: 215
+  Symbols:   759
+  CStrings:  600
 
Symbols:
+ -[WOWorkoutQueryServer remote_fetchConfigurationsCountWithCompletion:]
+ GCC_except_table23
+ GCC_except_table37
+ GCC_except_table47
+ _HDSQLEntityPropertyStar
+ ___70-[WOWorkoutQueryServer remote_fetchConfigurationsCountWithCompletion:]_block_invoke
+ ___block_descriptor_64_e8_32s40r48r_e35_B24?0"HDDatabaseTransaction"8^16lu56l8s32l8r40l8r48l8
+ _objc_msgSend$countValueForProperty:predicate:database:error:
+ _objc_msgSend$integerValue
- GCC_except_table45
CStrings:
+ "0A`"
+ "Failed to count workout configurations."
+ "[WorkoutQueryServer] counted %ld active and %ld deleted configuration, error: %{public}@"
+ "countValueForProperty:predicate:database:error:"
+ "integerValue"
+ "remote_fetchConfigurationsCountWithCompletion:"
+ "v24@0:8@?<v@?qq@\"NSError\">16"
```
