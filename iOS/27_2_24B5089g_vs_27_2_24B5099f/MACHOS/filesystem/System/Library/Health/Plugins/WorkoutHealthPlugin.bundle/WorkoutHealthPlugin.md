## WorkoutHealthPlugin

> `/System/Library/Health/Plugins/WorkoutHealthPlugin.bundle/WorkoutHealthPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2027.1.51.0.0
-  __TEXT.__text: 0x124a0
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_stubs: 0x1940
+2027.1.60.0.1
+  __TEXT.__text: 0x12424
+  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__objc_stubs: 0x1920
   __TEXT.__objc_methlist: 0xce4
   __TEXT.__cstring: 0x21cd
   __TEXT.__objc_classname: 0x1fb
-  __TEXT.__objc_methname: 0x236f
+  __TEXT.__objc_methname: 0x2365
   __TEXT.__objc_methtype: 0x953
-  __TEXT.__oslogstring: 0x1106
+  __TEXT.__oslogstring: 0x1130
   __TEXT.__gcc_except_tab: 0x300
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__unwind_info: 0x3c8
   __DATA_CONST.__const: 0xb18
   __DATA_CONST.__cfstring: 0x8c0
   __DATA_CONST.__objc_classlist: 0x50

   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x1e0
-  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x1a8
   __DATA.__objc_const: 0xdf0
-  __DATA.__objc_selrefs: 0x9e0
+  __DATA.__objc_selrefs: 0x9d8
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x420

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 213
+  Functions: 212
   Symbols:   741
-  CStrings:  594
+  CStrings:  593
 
Symbols:
+ _FISetWorkoutGymKitDetectionMode
+ _kNLConnectedGymPreferencesNFCDetectionMode
- ___os_log_helper_16_2_3_8_64_8_64_8_64
- _objc_msgSend$boolValue
Functions:
~ +[WOWorkoutGymKitNFCManager enableGymKitNFCDefaultForHopliteOOPIfNeeded] : 968 -> 948
- ___os_log_helper_16_2_3_8_64_8_64_8_64
CStrings:
+ "[WorkoutGymKitNFC] GymKit detection already set (mode=%@ legacy=%@), skipping seeding the default"
+ "[WorkoutGymKitNFC] One time Enable NFC Default For HopliteOOP, set %@ = AlwaysOn"
- "[WorkoutGymKitNFC] %@ already set to %@, skipping setting %@"
- "[WorkoutGymKitNFC] One time Enable NFC Default For HopliteOOP, set %@ = YES"
- "boolValue"
```
