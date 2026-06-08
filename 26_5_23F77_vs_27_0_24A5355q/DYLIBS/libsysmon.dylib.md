## libsysmon.dylib

> `/usr/lib/libsysmon.dylib`

```diff

-133.0.0.0.0
-  __TEXT.__text: 0x1784
-  __TEXT.__auth_stubs: 0x370
+135.0.0.0.0
+  __TEXT.__text: 0x1764
   __TEXT.__objc_methlist: 0x154
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x150
   __TEXT.__oslogstring: 0xb2
   __TEXT.__unwind_info: 0xe8
-  __TEXT.__objc_classname: 0x4a
-  __TEXT.__objc_methname: 0x147
-  __TEXT.__objc_methtype: 0xb5
-  __DATA_CONST.__got: 0x58
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__objc_const: 0x508
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x118
   __DATA.__data: 0x218
   __DATA_DIRTY.__objc_data: 0x28
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 82355776-048E-3B4D-A043-1D576582781F
+  UUID: 884082EC-E23F-3472-981F-E6C8DAEEC2E2
   Functions: 45
   Symbols:   202
-  CStrings:  64
+  CStrings:  19
 
Functions:
~ _sysmon_request_add_attribute : 316 -> 276
~ _sysmon_table_apply : 100 -> 104
~ -[OS_sysmon_table dealloc] : 132 -> 136
CStrings:
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "OS_sysmon_object"
- "OS_sysmon_request"
- "OS_sysmon_row"
- "OS_sysmon_table"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "description"
- "hash"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "superclass"
- "v16@0:8"
- "zone"

```
