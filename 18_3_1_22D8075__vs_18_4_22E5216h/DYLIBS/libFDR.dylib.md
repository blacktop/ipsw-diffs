## libFDR.dylib

> `/usr/lib/libFDR.dylib`

```diff

-1300.80.3.0.0
-  __TEXT.__text: 0x75cb4
-  __TEXT.__auth_stubs: 0x1300
-  __TEXT.__const: 0x1f80
-  __TEXT.__cstring: 0x210ba
+1300.100.55.0.0
+  __TEXT.__text: 0x81b38
+  __TEXT.__auth_stubs: 0x1370
+  __TEXT.__const: 0x1fe0
+  __TEXT.__cstring: 0x212b9
+  __TEXT.__gcc_except_tab: 0x28
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0xa60
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x9c8
+  __TEXT.__unwind_info: 0x1020
+  __TEXT.__objc_methname: 0x65
+  __TEXT.__objc_stubs: 0x80
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__const: 0x7a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x980
-  __AUTH_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__objc_selrefs: 0x20
+  __AUTH_CONST.__auth_got: 0x9c8
+  __AUTH_CONST.__auth_ptr: 0x38
   __AUTH_CONST.__const: 0x910
-  __AUTH_CONST.__cfstring: 0xe960
+  __AUTH_CONST.__cfstring: 0xea40
   __DATA.__data: 0x160
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0xc0
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 848
-  Symbols:   1235
-  CStrings:  3944
+  Functions: 4003
+  Symbols:   4567
+  CStrings:  3964
 
Symbols:
+ _AMSupportCreateDataFromMappedFileURL
+ _CFStringConvertEncodingToNSStringEncoding
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSString
+ __Unwind_Resume
+ ___objc_personality_v0
+ _objc_alloc
+ _objc_autorelease
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend
CStrings:
+ "*outValueData is NULL"
+ "AMFDRDataCopyPayloadKeysFromData"
+ "AMFDRDataCopyPayloadKeysFromData failed"
+ "AMFDRDataUtilitiesCreateDataWithBytesNoCopy"
+ "AMFDRDataUtilitiesCreateStringWithBytesNoCopy"
+ "AMFDRDataVerifyAndCopySubCCKeys"
+ "AMFDRSealingMapCopyLocalMinimalManifestSubCCKeys"
+ "AMFDRSealingMapCopyLocalSubCCKeys"
+ "CopyFromMappedFile"
+ "This is a proto device that needs more permissive decode options..."
+ "_AMFDRDataCopyFormattedRawAndImg4Internal"
+ "_AMFDRDataCreateUnsignedValue"
+ "_AMFDRSealingMapPrepareAMFDRForCopyLocalData"
+ "_AMFDRSealingMapPrepareAMFDRForCopyLocalData failed"
+ "_CFDataCreateFromData failed for *outImg4Data"
+ "_CFDataCreateFromData failed for *outManifest2"
+ "bytes not in binary range of data"
+ "currKeys allocation failed"
+ "data"
+ "decode and copy payload keys for %@ failed"
+ "failed to decode payload data as sysconfig format"
+ "iPhone17,1"
+ "iPhone17,2"
+ "iPhone17,3"
+ "iPhone17,4"
+ "initWithBytesNoCopy:length:deallocator:"
+ "initWithBytesNoCopy:length:encoding:deallocator:"
+ "invalid encoding: %@"
+ "localSubCCList is empty"
+ "manifest2 data is NULL"
+ "outPayloadKeys is NULL"
+ "outValueDataFormatted is NULL"
+ "string"
+ "v24@?0^v8Q16"
- "AMFDRDataDictCreateFromData failed"
- "CFDictionaryCreateMutable failed for copyLocalDataOptions"
- "This is a proto device, setting more permissive decode options..."
- "Unsupported multi action: %d"
- "Unsupported multi local action: %d"
- "_AMFDRDataCopyFormatted"
- "_AMFDRDataCopyFormattedRawAndImg4"
- "_AMFDRDataCreateUnsignedValueNoCopy"
- "_AMFDRSealingMapCopyLocalDataInternal"
- "decoded of %@ is NULL"
- "lo0"
- "pseudo_ccrng_allocate"
- "strippedManifest is NULL"
- "unexpected type for localManifestData: %@"

```
