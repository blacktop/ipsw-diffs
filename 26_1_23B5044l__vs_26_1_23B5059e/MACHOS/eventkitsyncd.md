## eventkitsyncd

> `/usr/libexec/eventkitsyncd`

```diff

-417.0.0.0.0
-  __TEXT.__text: 0x74680
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_stubs: 0xc500
-  __TEXT.__objc_methlist: 0x7240
-  __TEXT.__cstring: 0x5802
-  __TEXT.__objc_methname: 0xf394
-  __TEXT.__objc_classname: 0x8fa
+418.0.0.0.0
+  __TEXT.__text: 0x74b40
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__objc_stubs: 0xc620
+  __TEXT.__objc_methlist: 0x7288
+  __TEXT.__cstring: 0x58ef
+  __TEXT.__objc_methname: 0xf4f3
+  __TEXT.__objc_classname: 0x8fb
   __TEXT.__objc_methtype: 0x2480
   __TEXT.__const: 0x290
-  __TEXT.__oslogstring: 0xb912
-  __TEXT.__gcc_except_tab: 0xbb4
-  __TEXT.__unwind_info: 0x1650
-  __DATA_CONST.__auth_got: 0x6a0
+  __TEXT.__oslogstring: 0xb947
+  __TEXT.__gcc_except_tab: 0xc08
+  __TEXT.__unwind_info: 0x1668
+  __DATA_CONST.__auth_got: 0x6c0
   __DATA_CONST.__got: 0x408
-  __DATA_CONST.__const: 0x1798
-  __DATA_CONST.__cfstring: 0x4dc0
+  __DATA_CONST.__const: 0x17c0
+  __DATA_CONST.__cfstring: 0x4e40
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0xe9b8
-  __DATA.__objc_selrefs: 0x3d88
-  __DATA.__objc_ivar: 0x93c
+  __DATA.__objc_const: 0xea38
+  __DATA.__objc_selrefs: 0x3dd0
+  __DATA.__objc_ivar: 0x948
   __DATA.__objc_data: 0x1db0
   __DATA.__data: 0x800
   __DATA.__bss: 0x178

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0B3A55F0-E811-3D73-9F8D-7590B554DA1F
-  Functions: 2791
-  Symbols:   356
-  CStrings:  5302
+  UUID: 45DCA043-EDC7-3A0F-A748-2C5549768574
+  Functions: 2798
+  Symbols:   360
+  CStrings:  5326
 
Symbols:
+ _malloc_type_malloc
+ _os_state_add_handler
+ _os_state_remove_handler
+ _snprintf
CStrings:
+ "== Started EventKitSync-418"
+ "Completed checkin activity state for %s: %s"
+ "Error while generating state: %@"
+ "Exception while generating state: %@"
+ "NDTActivity '%s'"
+ "Starting checkin activity state for %s: %s"
+ "T@\"NSDate\",&,N,V_activityStateChangedDate"
+ "Tq,N,V_currentActivityState"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8"
+ "_activityStateChangedDate"
+ "_addStateHandler"
+ "_currentActivityState"
+ "_markActivityStateChanged:"
+ "_stateHandle"
+ "activityStateChangedDate"
+ "currentActivityState"
+ "dataWithPropertyList:format:options:error:"
+ "getBytes:length:"
+ "initWithFormat:"
+ "setActivityStateChangedDate:"
+ "setCurrentActivityState:"
- "&!"
- "== Started EventKitSync-417"
- "Checkin activity state for %s: %s"

```
