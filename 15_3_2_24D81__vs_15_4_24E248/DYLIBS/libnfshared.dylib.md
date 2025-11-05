## libnfshared.dylib

> `/usr/lib/libnfshared.dylib`

```diff

-353.3.0.0.0
-  __TEXT.__text: 0x23ccc
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x1834
-  __TEXT.__gcc_except_tab: 0x3ec
+354.27.0.0.0
+  __TEXT.__text: 0x24b78
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_methlist: 0x1d1c
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x3c7d
-  __TEXT.__oslogstring: 0x1753
   __TEXT.__dlopen_cstrs: 0x58
+  __TEXT.__cstring: 0x3dca
+  __TEXT.__oslogstring: 0x17b5
+  __TEXT.__gcc_except_tab: 0x460
   __TEXT.__unwind_info: 0x6b8
-  __TEXT.__objc_classname: 0x318
-  __TEXT.__objc_methname: 0x3cf1
-  __TEXT.__objc_methtype: 0x904
-  __TEXT.__objc_stubs: 0x2360
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x3f0
-  __DATA_CONST.__objc_classlist: 0x100
-  __DATA_CONST.__objc_catlist: 0x18
+  __TEXT.__objc_classname: 0x32c
+  __TEXT.__objc_methname: 0x3e27
+  __TEXT.__objc_methtype: 0x930
+  __TEXT.__objc_stubs: 0x2420
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__const: 0x3f8
+  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10a0
+  __DATA_CONST.__objc_selrefs: 0x1160
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xb8
-  __DATA_CONST.__objc_arraydata: 0x3f0
-  __AUTH_CONST.__auth_got: 0x570
-  __AUTH_CONST.__const: 0x5a0
-  __AUTH_CONST.__cfstring: 0x36c0
-  __AUTH_CONST.__objc_const: 0x3ce0
+  __DATA_CONST.__objc_arraydata: 0x3e8
+  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__const: 0x5c0
+  __AUTH_CONST.__cfstring: 0x37a0
+  __AUTH_CONST.__objc_const: 0x35a8
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x204
+  __AUTH.__objc_data: 0xa50
+  __DATA.__objc_ivar: 0x208
   __DATA.__data: 0x408
-  __DATA.__bss: 0x138
+  __DATA.__bss: 0x150
   __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 528D18C3-769E-31B9-B48A-7FFA90C1C94B
-  Functions: 646
-  Symbols:   1664
-  CStrings:  2124
+  UUID: 937FACA6-8986-3C0B-B225-D2DDF13E77C8
+  Functions: 649
+  Symbols:   1697
+  CStrings:  2160
 
Symbols:
+ +[NFAssertionCALogger postAnalyticsDefaultAppSupression:prepOnly:]
+ +[NFBackgroundActivityScheduler sharedBackgroundActivityScheduler]
+ +[NFCALogger roundToSignificantDigit:forValue:]
+ -[NFBackgroundActivityScheduler callbackMap]
+ -[NFBackgroundActivityScheduler getCallbacks:]
+ -[NFBackgroundActivityScheduler initCallbackArray:]
+ -[NFBackgroundActivityScheduler init]
+ -[NFBackgroundActivityScheduler registerCallback:identifier:]
+ -[NFBackgroundActivityScheduler setCallbackMap:]
+ -[NSString(HexString) NF_isPrefixOfHexEncodedEqualToBytes:length:]
+ GCC_except_table13
+ GCC_except_table16
+ GCC_except_table19
+ OBJC_IVAR_$_NFBackgroundActivityScheduler._callbackMap
+ _NFDataRelinquishOwnership
+ _NFIsSEinOFFSupported
+ _OBJC_CLASS_$_NFAssertionCALogger
+ _OBJC_METACLASS_$_NFAssertionCALogger
+ __120-[NFBackgroundActivityScheduler backgroundActivityScheduler:interval:tolerance:repeats:qualityOfService:delay:callback:]_block_invoke.14
+ __72-[NFBackgroundActivityScheduler schedulePreRegisteredActivity:callback:]_block_invoke.9
+ __NFPlatformGetSupportedLPMFlags
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_HexString
+ __OBJC_$_CATEGORY_NSString_$_HexString
+ __OBJC_$_CLASS_METHODS_NFAssertionCALogger
+ __OBJC_$_CLASS_METHODS_NFBackgroundActivityScheduler
+ __OBJC_CLASS_RO_$_NFAssertionCALogger
+ __OBJC_METACLASS_RO_$_NFAssertionCALogger
+ ___66+[NFBackgroundActivityScheduler sharedBackgroundActivityScheduler]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e15_v16?0?<v?q>8l
+ ___exp10
+ _log10
+ _objc_msgSend$callbackMap
+ _objc_msgSend$getCallbacks:
+ _objc_msgSend$initCallbackArray:
+ _objc_msgSend$initWithObjectsAndKeys:
+ _objc_msgSend$registerCallback:identifier:
+ _objc_msgSend$roundToSignificantDigit:forValue:
+ postAnalyticsDefaultAppSupression:prepOnly:.assertions
- -[NFBackgroundActivityScheduler initWithQueue:]
- GCC_except_table2
- __120-[NFBackgroundActivityScheduler backgroundActivityScheduler:interval:tolerance:repeats:qualityOfService:delay:callback:]_block_invoke.9
- __72-[NFBackgroundActivityScheduler schedulePreRegisteredActivity:callback:]_block_invoke.6
- ___block_descriptor_40_e8_32bs_e15_v16?0?<v?q>8l
- ___copy_helper_block_e8_32b
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
