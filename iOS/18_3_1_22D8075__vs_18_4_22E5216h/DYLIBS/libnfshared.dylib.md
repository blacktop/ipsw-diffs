## libnfshared.dylib

> `/usr/lib/libnfshared.dylib`

```diff

-353.4.0.0.0
-  __TEXT.__text: 0x26504
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_methlist: 0x1a04
-  __TEXT.__gcc_except_tab: 0x3e4
+354.25.0.0.0
+  __TEXT.__text: 0x27304
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_methlist: 0x1eec
   __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x3e2e
-  __TEXT.__oslogstring: 0x19ed
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x700
-  __TEXT.__objc_classname: 0x34a
-  __TEXT.__objc_methname: 0x41b4
-  __TEXT.__objc_methtype: 0x9f8
-  __TEXT.__objc_stubs: 0x2600
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x820
-  __DATA_CONST.__objc_classlist: 0x110
-  __DATA_CONST.__objc_catlist: 0x18
+  __TEXT.__cstring: 0x3f7b
+  __TEXT.__oslogstring: 0x1a4f
+  __TEXT.__gcc_except_tab: 0x45c
+  __TEXT.__unwind_info: 0x708
+  __TEXT.__objc_classname: 0x35e
+  __TEXT.__objc_methname: 0x42ea
+  __TEXT.__objc_methtype: 0xa24
+  __TEXT.__objc_stubs: 0x26c0
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__const: 0x828
+  __DATA_CONST.__objc_classlist: 0x118
+  __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1198
+  __DATA_CONST.__objc_selrefs: 0x1258
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xc8
-  __DATA_CONST.__objc_arraydata: 0x3f0
-  __AUTH_CONST.__auth_got: 0x678
+  __DATA_CONST.__objc_arraydata: 0x3e8
+  __AUTH_CONST.__auth_got: 0x690
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x38a0
-  __AUTH_CONST.__objc_const: 0x3fa0
+  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__cfstring: 0x3980
+  __AUTH_CONST.__objc_const: 0x3868
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x20c
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x210
   __DATA.__data: 0x3d0
+  __DATA.__bss: 0x8
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_ivar: 0x18
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x1a8
+  __DATA_DIRTY.__bss: 0x1b8
   __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 678
-  Symbols:   1004
-  CStrings:  1790
+  Functions: 682
+  Symbols:   1022
+  CStrings:  1819
 
Symbols:
+ _NFDataRelinquishOwnership
+ _NFIsSEinOFFSupported
+ _OBJC_CLASS_$_NFAssertionCALogger
+ _OBJC_METACLASS_$_NFAssertionCALogger
+ ___exp10
+ _log10
+ _objc_retain_x9
CStrings:
+ "%c[%{public}s %{public}s]:%i getActivity for identifier (%{public}@): nil, generated new activity: %{public}@"
+ "%s:%i Source is not hex encoded bytes"
+ "%s:%i prefixBytes is of invalid length=%ld"
+ "%{public}s:%i Source is not hex encoded bytes"
+ "%{public}s:%i prefixBytes is of invalid length=%ld"
+ "-[NSString(HexString) NF_isPrefixOfHexEncodedEqualToBytes:length:]"
+ "B32@0:8r*16Q24"
+ "NFAssertionCALogger"
+ "NF_isPrefixOfHexEncodedEqualToBytes:length:"
+ "PID"
+ "PassKit foreground presentment intent"
+ "Q32@0:8Q16Q24"
+ "T@\"NSMutableDictionary\",&,N,V_callbackMap"
+ "_NFPlatformGetSupportedLPMFlags"
+ "_callbackMap"
+ "callbackMap"
+ "com.apple.nfcd.assertionSupressDefaultAppPresentment"
+ "com.apple.nfcd.backgroundActivityScheduler"
+ "endTime"
+ "getCallbacks:"
+ "initCallbackArray:"
+ "initWithObjectsAndKeys:"
+ "lpm"
+ "postAnalyticsDefaultAppSupression:prepOnly:"
+ "registerCallback:identifier:"
+ "roundToSignificantDigit:forValue:"
+ "setCallbackMap:"
+ "sharedBackgroundActivityScheduler"
+ "startTime"
+ "totalDuration"
+ "v32@0:8@?16@24"
- "%c[%{public}s %{public}s]:%i getActivity for identifier (%{public}@): nil. Create a new activity: %{public}@"
- "initWithQueue:"
- "totalSecureElementCredentialSession"

```
