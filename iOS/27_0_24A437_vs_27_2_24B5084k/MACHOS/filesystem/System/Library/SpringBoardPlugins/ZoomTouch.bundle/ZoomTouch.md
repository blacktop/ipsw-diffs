## ZoomTouch

> `/System/Library/SpringBoardPlugins/ZoomTouch.bundle/ZoomTouch`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-909.1.0.0.0
-  __TEXT.__text: 0x3f48
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_stubs: 0xdc0
+913.3.0.0.0
+  __TEXT.__text: 0x4048
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_stubs: 0xde0
   __TEXT.__objc_methlist: 0x434
-  __TEXT.__const: 0x58
+  __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__cstring: 0x38f
-  __TEXT.__objc_methname: 0x10b4
+  __TEXT.__cstring: 0x394
+  __TEXT.__objc_methname: 0x10bb
   __TEXT.__objc_classname: 0x63
   __TEXT.__objc_methtype: 0x1c9
-  __TEXT.__unwind_info: 0x228
+  __TEXT.__oslogstring: 0x72
+  __TEXT.__unwind_info: 0x230
   __DATA_CONST.__const: 0x230
-  __DATA_CONST.__cfstring: 0x560
+  __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__auth_got: 0x270
   __DATA_CONST.__got: 0x108
   __DATA.__objc_const: 0x738
-  __DATA.__objc_selrefs: 0x508
+  __DATA.__objc_selrefs: 0x510
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0xe0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 109
-  Symbols:   424
-  CStrings:  286
+  Functions: 110
+  Symbols:   429
+  CStrings:  289
 
Symbols:
+ _ZOOMLogEvents
+ _ZOTReportUnresolvedDisplay
+ __os_log_error_impl
+ _objc_msgSend$length
+ _os_log_type_enabled
Functions:
+ _ZOTReportUnresolvedDisplay
CStrings:
+ "%{public}@: no delegate for displayID %u, so zoom can't act on gestures from that display. Registered: %{public}@"
+ "length"
+ "none"
```
