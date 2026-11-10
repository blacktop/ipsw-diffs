## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/Versions/A/CoreDuet`

```diff

-1971.0.0.0.0
-  __TEXT.__text: 0x18fa7c
+1977.0.0.0.0
+  __TEXT.__text: 0x1902cc
   __TEXT.__objc_methlist: 0x1119c
-  __TEXT.__cstring: 0x14c18
-  __TEXT.__const: 0x5a0
-  __TEXT.__oslogstring: 0x1810d
-  __TEXT.__gcc_except_tab: 0x6d14
+  __TEXT.__cstring: 0x14ca7
+  __TEXT.__const: 0x5b8
+  __TEXT.__oslogstring: 0x180c7
+  __TEXT.__gcc_except_tab: 0x6d30
   __TEXT.__dlopen_cstrs: 0xb6
-  __TEXT.__unwind_info: 0x5058
+  __TEXT.__unwind_info: 0x5068
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d28
+  __DATA_CONST.__objc_selrefs: 0x7d50
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x648
   __DATA_CONST.__objc_arraydata: 0x678
-  __DATA_CONST.__got: 0x1108
+  __DATA_CONST.__got: 0x1110
   __AUTH_CONST.__const: 0x49d0
-  __AUTH_CONST.__cfstring: 0x127c0
+  __AUTH_CONST.__cfstring: 0x127e0
   __AUTH_CONST.__objc_const: 0x21cd0
   __AUTH_CONST.__objc_intobj: 0x2028
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x5e8
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0x970
+  __AUTH_CONST.__auth_got: 0x980
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x4920
+  __AUTH.__objc_data: 0x48f8
   __DATA.__objc_ivar: 0x1658
   __DATA.__data: 0x1a40
   __DATA.__bss: 0xa28
   __DATA.__common: 0x38
-  __DATA_DIRTY.__objc_data: 0x2da0
+  __DATA_DIRTY.__objc_data: 0x2dc8
   __DATA_DIRTY.__bss: 0x450
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
+  - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8526
-  Symbols:   16014
-  CStrings:  4484
+  Functions: 8527
+  Symbols:   16025
+  CStrings:  4489
 
Symbols:
+ _CDStringByConvertingPhoneNumberStringToASCII
+ _CFStringNormalize
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ __CDNonASCIIDigitRangeStarts
+ __CDStringByConvertingPhoneNumberStringToASCII
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80r88r96r104r112r120r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80r88r96r104r112r120r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r88r96r104r112r120r
+ _kTCCServiceSiriAccess
+ _objc_msgSend$canBeConvertedToEncoding:
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$characterIsMember:
+ _objc_msgSend$initWithCharacters:length:
+ _objc_msgSend$nonBaseCharacterSet
- ___block_descriptor_120_e8_32s40s48s56s64s72r80r88r96r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64s72r80r88r96r
- ___destroy_helper_block_e8_32s40s48s56s64s72r80r88r96r
CStrings:
+ "AppExclusions"
+ "Error checking Siri Learning access (errno %{darwin.errno}d). Attempting checks but they may not work."
+ "IntelligenceFlow"
+ "Process has access to Siri Learning toggles."
+ "Unable to access Siri Learning toggles. Disabling checks."
+ "com.apple.tcc.access.changed"
+ "com.apple.tccd"
+ "creationDate > %@ OR (creationDate == %@ AND uuid > %@)"
+ "mach-lookup"
- "Creating shell PSC to truncate storage."
- "Error checking preferences access (errno %{darwin.errno}d). Attempting checks but they may not work."
- "Process has access to preferences for Siri Learning toggles."
- "Unable to access preferences for Siri Learning toggles. Disabling checks."
```
