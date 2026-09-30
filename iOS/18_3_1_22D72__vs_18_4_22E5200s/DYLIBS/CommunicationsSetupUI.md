## CommunicationsSetupUI

> `/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI`

```diff

-1500.400.111.0.0
-  __TEXT.__text: 0x8199c
+1500.500.111.0.0
+  __TEXT.__text: 0x824a4
   __TEXT.__auth_stubs: 0x1170
-  __TEXT.__objc_methlist: 0x7104
-  __TEXT.__cstring: 0xa667
-  __TEXT.__const: 0x484
-  __TEXT.__gcc_except_tab: 0x47a8
-  __TEXT.__oslogstring: 0x5907
+  __TEXT.__objc_methlist: 0x8194
+  __TEXT.__cstring: 0xa7c7
+  __TEXT.__const: 0x4c4
+  __TEXT.__gcc_except_tab: 0x4818
+  __TEXT.__oslogstring: 0x5a6d
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__ustring: 0x40
-  __TEXT.__swift5_typeref: 0x27e
+  __TEXT.__swift5_typeref: 0x250
   __TEXT.__swift5_reflstr: 0x45
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__constg_swiftt: 0x154
   __TEXT.__swift5_fieldmd: 0xd8
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x2638
+  __TEXT.__unwind_info: 0x2660
   __TEXT.__objc_classname: 0x1038
-  __TEXT.__objc_methname: 0x140a1
-  __TEXT.__objc_methtype: 0x37d9
-  __TEXT.__objc_stubs: 0xfbe0
-  __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__const: 0x1088
+  __TEXT.__objc_methname: 0x14161
+  __TEXT.__objc_methtype: 0x381a
+  __TEXT.__objc_stubs: 0xfc40
+  __DATA_CONST.__got: 0xa98
+  __DATA_CONST.__const: 0x10f8
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e30
+  __DATA_CONST.__objc_selrefs: 0x5498
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0x8c8
-  __AUTH_CONST.__auth_ptr: 0x150
+  __AUTH_CONST.__auth_ptr: 0x148
   __AUTH_CONST.__const: 0x900
-  __AUTH_CONST.__cfstring: 0xa320
-  __AUTH_CONST.__objc_const: 0xea90
+  __AUTH_CONST.__cfstring: 0xa400
+  __AUTH_CONST.__objc_const: 0xcc58
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1dd8
   __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0x528
-  __DATA.__data: 0xe58
+  __DATA.__data: 0xe50
   __DATA.__bss: 0x648
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2773
-  Symbols:   3348
-  CStrings:  5712
+  Functions: 2800
+  Symbols:   3383
+  CStrings:  5733
 
Symbols:
+ _kRegulatoryDomainUpdateNotification
- __swift_FORCE_LOAD_$_swiftFileProvider
CStrings:
+ "@\"UIConversationContext\"16@0:8"
+ "Domain: %@ wanted to show the online safety link"
+ "ONLINE SAFETY: Checking if region estimate %@ requires safety URL to be shown..."
+ "ONLINE SAFETY: Failed to open safety URL because it was not valid"
+ "ONLINE SAFETY: No valid safety URL was found for any of user's region estimates"
+ "ONLINE SAFETY: Opening safety URL..."
+ "ONLINE SAFETY: Removing specifier: %@"
+ "ONLINE SAFETY: Successfully opened safety URL!"
+ "ONLINE SAFETY: Valid safety URL found for region %@!"
+ "ONLINE SAFETY: shouldShowOnlineSafetyLink %d since device is not iPad %d and safety URL is valid %d"
+ "ONLINE_SAFETY_GROUP_ID"
+ "ONLINE_SAFETY_ID"
+ "T@\"UIConversationContext\",?,&,N"
+ "UK"
+ "UK_ONLINE_SAFETY_URL"
+ "Unable to determine region, defaulting to not showing online safety link"
+ "Zelkova_Korea"
+ "_onlineSafetyGroupSpecifiers"
+ "_onlineSafetyRegionCodesURLMapping"
+ "_safetyURLForCurrentRegion"
+ "_safetyURLForCurrentRegionIfAny"
+ "conversationContext"
+ "currentRegionWantsOnlineSafetyLink"
+ "deselectRowAtIndexPath:animated:"
+ "https://www.apple.com/au/legal/online-safety/"
+ "https://www.apple.com/uk/legal/online-safety/"
+ "onlineSafetyRegionCodesURLMapping"
+ "openOnlineSafetyURL"
+ "setConversationContext:"
+ "v24@0:8@\"UIConversationContext\"16"
- "AU ESAFETY: Cannot launch AU eSafety Act URL because URL is nil"
- "AU ESAFETY: Checking current locale... %@ to %@"
- "AU ESAFETY: Current locale is AU and device is phone, show AU eSafety link"
- "AU ESAFETY: Launching AU eSafety Act URL %@"
- "AU ESAFETY: Removing specifier: %@"
- "AU_ONLINE_SAFETY_GROUP_ID"
- "AU_ONLINE_SAFETY_ID"
- "_australiaOnlineSafetyGroupSpecifiers"
- "_openAUOnlineSafetyURL"
- "openAUOnlineSafetyURL"
- "regionCode"
- "shouldShowAUOnlineSafetySpecifiers"

```
