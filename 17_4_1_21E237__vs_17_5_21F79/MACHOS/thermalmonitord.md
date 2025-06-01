## thermalmonitord

> `/usr/libexec/thermalmonitord`

```diff

-1952.100.8.0.0
-  __TEXT.__text: 0x560e0
-  __TEXT.__auth_stubs: 0x13f0
-  __TEXT.__objc_stubs: 0x50e0
-  __TEXT.__objc_methlist: 0x3c98
+1952.120.7.0.0
+  __TEXT.__text: 0x56ab8
+  __TEXT.__auth_stubs: 0x1420
+  __TEXT.__objc_stubs: 0x5180
+  __TEXT.__objc_methlist: 0x3cc8
   __TEXT.__const: 0x1900
   __TEXT.__objc_classname: 0xf10
-  __TEXT.__objc_methname: 0x868f
+  __TEXT.__objc_methname: 0x8733
   __TEXT.__objc_methtype: 0x1894
   __TEXT.__gcc_except_tab: 0x3c4
-  __TEXT.__cstring: 0x4bbd
-  __TEXT.__oslogstring: 0x85ea
+  __TEXT.__cstring: 0x4bdd
+  __TEXT.__oslogstring: 0x8812
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x10ac
-  __DATA_CONST.__auth_got: 0xa10
+  __TEXT.__unwind_info: 0x1128
+  __DATA_CONST.__auth_got: 0xa28
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1460
-  __DATA_CONST.__cfstring: 0x6120
+  __DATA_CONST.__cfstring: 0x6160
   __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x4c8
+  __DATA_CONST.__objc_classrefs: 0x4d0
   __DATA_CONST.__objc_superrefs: 0x2f0
   __DATA_CONST.__objc_intobj: 0x768
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x1c8
-  __DATA.__objc_const: 0xc5a8
-  __DATA.__objc_selrefs: 0x1928
-  __DATA.__objc_ivar: 0xa94
+  __DATA.__objc_const: 0xc5e8
+  __DATA.__objc_selrefs: 0x1958
+  __DATA.__objc_ivar: 0xa9c
   __DATA.__objc_data: 0x2a30
   __DATA.__data: 0x3c8
-  __DATA.__bss: 0x7468
-  __DATA.__common: 0x9e4
+  __DATA.__bss: 0x7474
+  __DATA.__common: 0x9f0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
+  - /System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C0457DD-F0A5-3315-B0E2-2A44E39CA5F1
-  Functions: 2091
-  Symbols:   414
-  CStrings:  4399
+  UUID: FDE10C66-0B8F-329F-BF6C-C29469ECAFEE
+  Functions: 2107
+  Symbols:   418
+  CStrings:  4422
 
Symbols:
+ _IOHIDEventCreateKeyboardEvent
+ _IOHIDEventSystemCopyEvent
+ _IOHIDEventSystemCreate
+ _OBJC_CLASS_$_CLPCPolicyInterface
CStrings:
+ "<Error> Couldn't create hidEventSystem"
+ "<Error> Error creating CLPC client %@"
+ "<Error> Error setting dock mode to True with folio attached %@"
+ "<Error> Error setting dock mode to True with keyboard attached %@"
+ "<Error> Error setting dock mode to false in CLPC client %@"
+ "<Error> Failed to copy keyboard event from client"
+ "<Error> Unable to create eventRef for keyboard event"
+ "<Error> Unable to get HID services for folio detection"
+ "<Notice> KeyboardHelper updating SDTK - NewValue: %u PreviousValue: %u"
+ "<Notice> Uses CLPC framework"
+ "<Notice> Using Folio Helper"
+ "<Notice> Using Keyboard Helper"
+ "_cachedIsFolioAttached"
+ "_hidClient"
+ "createClient:"
+ "getInitialFolioState"
+ "needsCLPCClient"
+ "registerForFolioEvents"
+ "setDockMode:options:error:"
+ "updateFolioState:"
+ "updateSensorExchangeKey"
+ "usesFolioHelper"
- "<Notice> Using KeyboardHelper"

```
