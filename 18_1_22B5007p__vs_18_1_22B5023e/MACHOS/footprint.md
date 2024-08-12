## footprint

> `/usr/bin/footprint`

```diff

-272.0.0.0.0
-  __TEXT.__text: 0x19a60
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_stubs: 0x2200
-  __TEXT.__objc_methlist: 0xe08
-  __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x3c0
-  __TEXT.__cstring: 0x2fcd
-  __TEXT.__objc_methname: 0x22a4
+276.0.0.0.0
+  __TEXT.__text: 0x19c94
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_stubs: 0x2260
+  __TEXT.__objc_methlist: 0xe3c
+  __TEXT.__const: 0xe8
+  __TEXT.__gcc_except_tab: 0x3c4
+  __TEXT.__cstring: 0x2fde
+  __TEXT.__objc_methname: 0x22f1
   __TEXT.__objc_classname: 0x1fa
-  __TEXT.__objc_methtype: 0x792
+  __TEXT.__objc_methtype: 0x79e
   __TEXT.__ustring: 0xd0
+  __TEXT.__oslogstring: 0x21
   __TEXT.__info_plist: 0x4b0
-  __TEXT.__unwind_info: 0x480
-  __DATA_CONST.__auth_got: 0x610
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x16b8
-  __DATA_CONST.__cfstring: 0x2080
+  __TEXT.__unwind_info: 0x490
+  __DATA_CONST.__auth_got: 0x628
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x16d8
+  __DATA_CONST.__cfstring: 0x20a0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x33a8
-  __DATA.__objc_selrefs: 0x928
-  __DATA.__objc_ivar: 0x27c
+  __DATA.__objc_const: 0x33d8
+  __DATA.__objc_selrefs: 0x940
+  __DATA.__objc_ivar: 0x280
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x248
   __DATA.__bss: 0x4140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 407
-  Symbols:   268
-  CStrings:  1131
+  Functions: 411
+  Symbols:   272
+  CStrings:  1139
 
Symbols:
+ __os_log_default
+ __os_log_error_impl
+ _memorystatus_control
+ _os_log_type_enabled
CStrings:
+ "I20@0:8I16"
+ "Ti,R,N,V_priority"
+ "Tr*,R,N"
+ "Unable to fetch process info: %!d(MISSING)"
+ "_dirtyFlagsFromEntryState:"
+ "_gatherProcessState"
+ "_priority"
+ "_setPriority:"
+ "jetsam priority"
+ "priority"
+ "r*16@0:8"
+ "r*16@?0q8"
- "*16@0:8"
- "*16@?0q8"
- "T*,R,N"
- "_gatherIdleExitStatus"

```
