## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2180.4.1.2.0
-  __TEXT.__text: 0x79abb0
+2190.1.1.0.0
+  __TEXT.__text: 0x79abd4
   __TEXT.__auth_stubs: 0x5640
   __TEXT.__objc_methlist: 0x35d10
   __TEXT.__const: 0xc780
-  __TEXT.__cstring: 0x8fa87
-  __TEXT.__oslogstring: 0x10fdb2
+  __TEXT.__cstring: 0x8fa85
+  __TEXT.__oslogstring: 0x10fdba
   __TEXT.__gcc_except_tab: 0x2b44
   __TEXT.__ustring: 0x2d4
   __TEXT.__unwind_info: 0x10920
   __TEXT.__objc_classname: 0x4ed7
   __TEXT.__objc_methname: 0x7e1fb
   __TEXT.__objc_methtype: 0x283d7
-  __TEXT.__objc_stubs: 0x4f0c0
+  __TEXT.__objc_stubs: 0x4f100
   __DATA_CONST.__got: 0x1a60
   __DATA_CONST.__const: 0x6b38
   __DATA_CONST.__objc_classlist: 0x12f0

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8DE41185-2E97-3577-9482-80ED543710E5
+  UUID: F1EEFCF4-CD92-3466-A191-37903B633016
   Functions: 31655
-  Symbols:   97613
+  Symbols:   97615
   CStrings:  57391
 
Symbols:
+ _objc_msgSend$setupLocalABTestSwitches
+ _objc_msgSend$setupLocalOnOffSwitches
Functions:
~ -[VCSwitchManager initializeLocalSwitches] : 472 -> 508
CStrings:
+ " [%s] %s:%d SwitchManager: A/B testing turned off - using master local switch: %08X"
+ "2190.1.1"
- " [%s] %s:%d SwitchManager: Non-seed build - using master local switch: %08X"
- "2180.4.1.2"

```
