## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-335.1.0.0.0
-  __TEXT.__text: 0xb63f8
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x10590
+336.1.0.0.0
+  __TEXT.__text: 0xb7ae4
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_methlist: 0x10640
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x5825
+  __TEXT.__cstring: 0x5913
   __TEXT.__gcc_except_tab: 0x568
-  __TEXT.__oslogstring: 0x2e0d
+  __TEXT.__oslogstring: 0x2ed6
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x2df8
-  __TEXT.__objc_classname: 0x2dba
-  __TEXT.__objc_methname: 0x15a35
-  __TEXT.__objc_methtype: 0x3161
-  __TEXT.__objc_stubs: 0xe9e0
+  __TEXT.__unwind_info: 0x2e38
+  __TEXT.__objc_classname: 0x2dca
+  __TEXT.__objc_methname: 0x15b32
+  __TEXT.__objc_methtype: 0x31c0
+  __TEXT.__objc_stubs: 0xea60
   __DATA_CONST.__got: 0x9b0
-  __DATA_CONST.__const: 0x1cd8
-  __DATA_CONST.__objc_classlist: 0x988
+  __DATA_CONST.__const: 0x1d00
+  __DATA_CONST.__objc_classlist: 0x990
   __DATA_CONST.__objc_nlclslist: 0x6e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x540
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x58c8
+  __DATA_CONST.__objc_selrefs: 0x5910
   __DATA_CONST.__objc_protorefs: 0x4e0
-  __DATA_CONST.__objc_superrefs: 0xce0
+  __DATA_CONST.__objc_superrefs: 0xce8
   __DATA_CONST.__objc_arraydata: 0x6dc8
-  __AUTH_CONST.__auth_got: 0x300
-  __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__cfstring: 0xa520
-  __AUTH_CONST.__objc_const: 0x3f8a8
+  __AUTH_CONST.__auth_got: 0x338
+  __AUTH_CONST.__const: 0x8e0
+  __AUTH_CONST.__cfstring: 0xa560
+  __AUTH_CONST.__objc_const: 0x3fa38
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x3e30
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x1720
-  __DATA.__objc_ivar: 0x4a8
+  __DATA.__objc_ivar: 0x4b8
   __DATA.__data: 0x3f20
-  __DATA.__bss: 0x308
-  __DATA_DIRTY.__objc_data: 0x4830
+  __DATA.__bss: 0x348
+  __DATA_DIRTY.__objc_data: 0x4880
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5619
-  Symbols:   6904
-  CStrings:  6098
+  Functions: 5643
+  Symbols:   6937
+  CStrings:  6129
 
Symbols:
+ _CAFStateCaptureLogging
+ _OBJC_CLASS_$_CAFStateCapture
+ _OBJC_METACLASS_$_CAFStateCapture
+ _OPACKEncoderCreateData
+ ___strlcpy_chk
+ _class_getName
+ _malloc_type_calloc
+ _memcpy
+ _os_state_add_handler
+ _os_state_remove_handler
CStrings:
+ "%!@(MISSING) %!s(MISSING)"
+ "%!@(MISSING) %!s(MISSING) disabled"
+ "%!@(MISSING) Error serializing dictionary for State Capture: %!d(MISSING)"
+ "%!@(MISSING) captured state data.length=%!l(MISSING)u"
+ "%!@(MISSING) failed to create state"
+ "%!@(MISSING) got called os_state_add_handler"
+ "%!@(MISSING) over data limit, length=%!l(MISSING)u"
+ "-[CAFStateCapture initWithIdentifier:capture:]"
+ "<%!@(MISSING): %!p(MISSING) identifier=%!@(MISSING)>"
+ "@32@0:8@16@?24"
+ "CAFStateCapture"
+ "StateCapture"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSSet\",R,N"
+ "T@\"NSString\",R,N,V_identifier"
+ "T@?,C,N,V_capture"
+ "TQ,N,V_handler"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@0:8"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8"
+ "_capture"
+ "_queue"
+ "bytes"
+ "capture"
+ "com.apple.caraccessoryframework.StateCapture-%!@(MISSING)-%!p(MISSING)"
+ "initWithIdentifier:capture:"
+ "queue"
+ "setCapture:"
+ "setQueue:"
+ "setWithArray:"
+ "stateCapture"
+ "stateCaptureValues"

```
