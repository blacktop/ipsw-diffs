## UserProfilesCore

> `/System/Library/PrivateFrameworks/UserProfilesCore.framework/UserProfilesCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-299.0.7.0.0
-  __TEXT.__text: 0xa110
-  __TEXT.__objc_methlist: 0xd4c
+299.0.11.0.0
+  __TEXT.__text: 0xb48c
+  __TEXT.__objc_methlist: 0xe34
   __TEXT.__const: 0x2b6
-  __TEXT.__cstring: 0x827
-  __TEXT.__oslogstring: 0x8a0
+  __TEXT.__cstring: 0x9d7
+  __TEXT.__oslogstring: 0x9e0
   __TEXT.__gcc_except_tab: 0xc8
   __TEXT.__swift5_typeref: 0x150
   __TEXT.__swift5_fieldmd: 0xc4

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x418
+  __TEXT.__unwind_info: 0x498
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2f8
-  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__const: 0x348
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x910
-  __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__objc_selrefs: 0x998
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__got: 0x1a8
   __AUTH_CONST.__const: 0x278
-  __AUTH_CONST.__cfstring: 0x960
-  __AUTH_CONST.__objc_const: 0x2e50
+  __AUTH_CONST.__cfstring: 0xb40
+  __AUTH_CONST.__objc_const: 0x3320
   __AUTH_CONST.__auth_got: 0x400
-  __AUTH.__objc_data: 0x500
+  __AUTH.__objc_data: 0x550
   __AUTH.__data: 0x20
-  __DATA.__objc_ivar: 0xb4
+  __DATA.__objc_ivar: 0xb8
   __DATA.__data: 0x550
   __DATA.__bss: 0x130
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 377
-  Symbols:   976
-  CStrings:  122
+  Functions: 419
+  Symbols:   1030
+  CStrings:  144
 
Symbols:
+ -[UPSoftwareVersion isAfter:]
+ -[UPSoftwareVersion isBefore:]
+ -[UPSoftwareVersion isSameAs:]
+ -[UPSoftwareVersion isSameAsOrAfter:]
+ -[UPSoftwareVersion isSameAsOrBefore:]
+ -[UPSystemVersion .cxx_destruct]
+ -[UPSystemVersion buildVersion]
+ -[UPSystemVersion copyWithZone:]
+ -[UPSystemVersion debugDescription]
+ -[UPSystemVersion descriptionBuilderWithMultilinePrefix:]
+ -[UPSystemVersion descriptionWithMultilinePrefix:]
+ -[UPSystemVersion description]
+ -[UPSystemVersion hash]
+ -[UPSystemVersion initWithVersion:buildVersion:]
+ -[UPSystemVersion initWithVersionString:buildVersionString:]
+ -[UPSystemVersion isEqual:]
+ -[UPSystemVersion succinctDescriptionBuilder]
+ -[UPSystemVersion succinctDescription]
+ -[UPSystemVersion version]
+ _OBJC_CLASS_$_BSBuildVersion
+ _OBJC_CLASS_$_UPSystemVersion
+ _OBJC_IVAR_$_UPSystemVersion._buildVersion
+ _OBJC_IVAR_$_UPSystemVersion._version
+ _OBJC_METACLASS_$_UPSystemVersion
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_INSTANCE_METHODS_UPSystemVersion
+ __OBJC_$_INSTANCE_VARIABLES_UPSystemVersion
+ __OBJC_$_PROP_LIST_UPSystemVersion
+ __OBJC_CLASS_PROTOCOLS_$_UPSystemVersion
+ __OBJC_CLASS_RO_$_UPSystemVersion
+ __OBJC_METACLASS_RO_$_UPSystemVersion
+ ___27-[UPSystemVersion isEqual:]_block_invoke
+ ___27-[UPSystemVersion isEqual:]_block_invoke_2
+ ___57-[UPSystemVersion descriptionBuilderWithMultilinePrefix:]_block_invoke
+ ___57-[UPSystemVersion descriptionBuilderWithMultilinePrefix:]_block_invoke_2
+ ___57-[UPSystemVersion descriptionBuilderWithMultilinePrefix:]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e21_"BSBuildVersion"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e24_"UPSoftwareVersion"8?0ls32l8
+ _objc_msgSend$activeMultilinePrefix
+ _objc_msgSend$appendInteger:withName:
+ _objc_msgSend$appendString:
+ _objc_msgSend$classForCoder
+ _objc_msgSend$initWithVersion:buildVersion:
+ _objc_msgSend$initWithVersionString:buildVersionString:
+ _objc_msgSend$isAfter:withPrecision:
+ _objc_msgSend$isBefore:withPrecision:
+ _objc_msgSend$isSameAs:withPrecision:
+ _objc_msgSend$isSameAsOrAfter:withPrecision:
+ _objc_msgSend$isSameAsOrBefore:withPrecision:
+ _objc_msgSend$majorBuildLetterString
+ _objc_msgSend$majorBuildNumber
+ _objc_msgSend$minorBuildLetterString
+ _objc_msgSend$minorBuildNumber
+ _objc_msgSend$stringByAppendingFormat:
- -[UPPlatform buildVersion]
- _OBJC_IVAR_$_UPPlatform._buildVersion
CStrings:
+ "\""
+ "%@%lu"
+ "%lu%@%lu"
+ "@\"BSBuildVersion\"8@?0"
+ "@\"UPSoftwareVersion\"8@?0"
+ "BSBuildVersion"
+ "MobileGestalt returned no build version."
+ "MobileGestalt returned no product type."
+ "MobileGestalt returned no system version."
+ "UPSoftwareVersion"
+ "UPSystemVersion.m"
+ "Unable to create system version from strings. systemVersionString=%{public}@, buildVersionString=%{public}@"
+ "Unable to parse system version. versionString=%{public}@, buildVersionString=%{public}@"
+ "Value for '%@' was of unexpected class %@. Expected %@."
+ "Value for '%@' was unexpectedly nil. Expected %@."
+ "[_bs_assert_object isKindOfClass:BSBuildVersionClass]"
+ "[_bs_assert_object isKindOfClass:UPSoftwareVersionClass]"
+ "buildVersionString"
+ "majorBuildLetterString"
+ "majorBuildNumber"
+ "minorBuildLetterString"
+ "minorBuildNumber"
+ "version"
+ "versionString"
- "#"
- "%lu%@%lu%@%lu"
```
