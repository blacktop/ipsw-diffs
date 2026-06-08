## SPRCore

> `/System/Library/PrivateFrameworks/SPRCore.framework/SPRCore`

```diff

-44.13.0.0.0
-  __TEXT.__text: 0x21208
-  __TEXT.__auth_stubs: 0x1480
+50.27.0.0.0
+  __TEXT.__text: 0x22c10
   __TEXT.__objc_methlist: 0x170
-  __TEXT.__const: 0xe14
-  __TEXT.__cstring: 0x3eb
+  __TEXT.__const: 0x1014
+  __TEXT.__cstring: 0x3fb
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__oslogstring: 0x27d
-  __TEXT.__constg_swiftt: 0x3e0
-  __TEXT.__swift5_typeref: 0x3c5
-  __TEXT.__swift5_proto: 0x84
-  __TEXT.__swift5_types: 0x44
+  __TEXT.__oslogstring: 0x39d
+  __TEXT.__constg_swiftt: 0x454
+  __TEXT.__swift5_typeref: 0x3df
+  __TEXT.__swift5_proto: 0x90
+  __TEXT.__swift5_types: 0x50
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift_as_entry: 0x24
-  __TEXT.__swift_as_ret: 0x24
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift_as_cont: 0x58
   __TEXT.__unwind_info: 0x920
-  __TEXT.__eh_frame: 0x1308
-  __TEXT.__objc_classname: 0xb3
-  __TEXT.__objc_methname: 0x4d4
-  __TEXT.__objc_methtype: 0x164
-  __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__eh_frame: 0x1258
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c0
-  __AUTH_CONST.__auth_got: 0xa50
-  __AUTH_CONST.__const: 0x820
-  __AUTH_CONST.__cfstring: 0xa0
-  __AUTH_CONST.__objc_const: 0x510
+  __DATA_CONST.__objc_selrefs: 0x1e0
+  __DATA_CONST.__got: 0x320
+  __AUTH_CONST.__const: 0xa98
+  __AUTH_CONST.__cfstring: 0xc0
+  __AUTH_CONST.__objc_const: 0x5a0
+  __AUTH_CONST.__auth_got: 0xb58
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x208
-  __DATA.__data: 0x5f8
-  __DATA.__bss: 0xe40
+  __AUTH.__data: 0x2a0
+  __DATA.__data: 0x688
+  __DATA.__bss: 0xfc0
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 87609F3C-1438-3CC8-9426-C0B8260860A6
-  Functions: 797
-  Symbols:   186
-  CStrings:  133
+  UUID: 0641F1D2-96D4-305A-B965-7F9369BD60E8
+  Functions: 826
+  Symbols:   209
+  CStrings:  58
 
Symbols:
+ _NFCDErrorDomain
+ _OBJC_CLASS_$_NFSecureElement
+ _memset
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_task_addCancellationHandler
+ _swift_task_future_wait_throwing
+ _swift_task_removeCancellationHandler
+ _swift_willThrowTypedImpl
- _objc_release_x27
- _objc_release_x28
- _objc_retain_x23
- _swift_release_n
CStrings:
+ "Bad APDU response when selecting the PTC applet."
+ "Could not access the SE: %@"
+ "Could not select the PTC applet."
+ "Failed to get the result from the PTC applet."
+ "Failed to run the APDU command for the PTC applet."
+ "LEGACY"
+ "NFSecureElementManagerSession start timed out"
+ "NFSecureElementReaderSession start timed out"
+ "NFTrust"
+ "SES"
+ "nfcd"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@32@0:8Q16^@24"
- "@32@0:8d16^@24"
- "B16@0:8"
- "B32@0:8@16^B24"
- "Bool"
- "Deadline"
- "Decimal"
- "HexString"
- "NFSecureElementManagerSession timed out"
- "SPRLogger"
- "SPRSSEWrapper"
- "Scalar"
- "T@\"NSObject<OS_os_log>\",R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "UTF8String"
- "_TtC7SPRCore15DERMemoryWriter"
- "_TtC7SPRCore20NFSessionCancelState"
- "_TtC7SPRCore23FeedbackFrameworkString"
- "appendFormat:"
- "asHexString"
- "boolForKey:valid:"
- "boolStringValue"
- "boolValue"
- "bundleForClass:"
- "bytes"
- "close"
- "d32@0:8@16^B24"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithHexString:"
- "decimalForKey:valid:"
- "decimalNumberWithDecimal:"
- "decimalValue"
- "decodeDecimalForKey:"
- "decodeObjectOfClass:forKey:"
- "doubleForKey:valid:"
- "doubleValue"
- "encodeDecimal:forKey:"
- "encodeObject:forKey:"
- "endSession"
- "errorWithDomain:code:userInfo:"
- "evaluateWithObject:"
- "getBuffer:length:"
- "getSignedDeviceData:"
- "initWithData:"
- "initWithString:"
- "integerForKey:valid:"
- "integerValue"
- "isAtEnd"
- "isFeatureAppleSSESupported"
- "isFirstInQueue"
- "length"
- "lock"
- "memory"
- "notANumber"
- "objectForKey:"
- "open"
- "pinCryptoObjC"
- "q32@0:8@16^B24"
- "read:maxLength:"
- "secureElementObjC"
- "setCharactersToBeSkipped:"
- "startSecureElementManagerSession:"
- "startSecureElementManagerSessionAndReturnError:"
- "startSecureElementManagerSessionWithDeadline:error:"
- "startSecureElementManagerSessionWithTimeout:error:"
- "startSecureElementReaderSession:"
- "startSecureElementReaderSessionAndReturnError:"
- "startSecureElementReaderSessionWithDeadline:error:"
- "startSecureElementReaderSessionWithTimeout:error:"
- "streamError"
- "stringWithBool:"
- "stringWithCapacity:"
- "subsystem"
- "v44@0:8{?=b8b4b1b1b18[8S]}16@36"
- "write:maxLength:"
- "xpcClient"
- "{?=b8b4b1b1b18[8S]}24@0:8@16"
- "{?=b8b4b1b1b18[8S]}32@0:8@16^B24"

```
