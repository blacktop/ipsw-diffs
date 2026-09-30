## AirDropAlertUI

> `/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDropAlertUI.appex/AirDropAlertUI`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2124.10.2.2.2
-  __TEXT.__text: 0x1dec
-  __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_stubs: 0x920
+2126.10.4.0.0
+  __TEXT.__text: 0x21d8
+  __TEXT.__auth_stubs: 0x300
+  __TEXT.__objc_stubs: 0x960
   __TEXT.__objc_methlist: 0x27c
-  __TEXT.__const: 0x48
-  __TEXT.__objc_methname: 0x84c
-  __TEXT.__oslogstring: 0x206
+  __TEXT.__const: 0x50
+  __TEXT.__objc_methname: 0x89b
+  __TEXT.__oslogstring: 0x29c
   __TEXT.__cstring: 0x67
   __TEXT.__objc_classname: 0x8e
   __TEXT.__objc_methtype: 0x250

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__auth_got: 0x190
   __DATA_CONST.__got: 0x60
-  __DATA.__objc_const: 0x4e8
-  __DATA.__objc_selrefs: 0x340
-  __DATA.__objc_ivar: 0x3c
+  __DATA.__objc_const: 0x528
+  __DATA.__objc_selrefs: 0x350
+  __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 43
-  Symbols:   73
-  CStrings:  191
+  Symbols:   76
+  CStrings:  201
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _os_signpost_enabled
+ _os_signpost_id_make_with_pointer
Functions:
~ sub_100000ea0 : 1120 -> 1416
~ sub_100001300 -> sub_100001428 : 76 -> 380
~ sub_100001720 -> sub_100001978 : 184 -> 588
CStrings:
+ " enableTelemetry=YES "
+ "Alert.Decision.Accept"
+ "Alert.Decision.Decline"
+ "Alert.Present"
+ "Alert.UserDecision"
+ "_signpostAlertPresentBegan"
+ "_signpostUserDecisionBegan"
+ "length"
+ "substringToIndex:"
+ "transferID=%{public, signpost.telemetry:string1}@"
```
