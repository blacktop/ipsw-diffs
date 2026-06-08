## CoreTime

> `/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime`

```diff

-334.0.16.3.0
-  __TEXT.__text: 0x62ac
-  __TEXT.__auth_stubs: 0x4a0
+340.0.8.0.0
+  __TEXT.__text: 0x6854
   __TEXT.__objc_methlist: 0x28c
-  __TEXT.__const: 0xf8
+  __TEXT.__const: 0xf0
   __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__cstring: 0xe0c
-  __TEXT.__oslogstring: 0x4ba
+  __TEXT.__cstring: 0xee9
+  __TEXT.__oslogstring: 0x504
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0x248
-  __TEXT.__objc_classname: 0x5a
-  __TEXT.__objc_methname: 0x5d2
-  __TEXT.__objc_methtype: 0x103
-  __TEXT.__objc_stubs: 0x5e0
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x580
+  __TEXT.__unwind_info: 0x250
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x598
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x228
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x260
+  __DATA_CONST.__got: 0xa0
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0xe00
   __AUTH_CONST.__objc_const: 0x3c8
-  __AUTH_CONST.__objc_intobj: 0x4f8
+  __AUTH_CONST.__objc_intobj: 0x4e0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0x120
   __DATA.__bss: 0x68

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C8AE2807-9DD6-38FF-8F3E-D326B564205E
-  Functions: 188
-  Symbols:   739
-  CStrings:  426
+  UUID: C7F80A22-EF07-3521-97EB-49E2F1E7B6BF
+  Functions: 195
+  Symbols:   749
+  CStrings:  317
 
Symbols:
+ GCC_except_table31
+ GCC_except_table38
+ _TMAutoSetTimeNotification
+ _TMDidFinishSetup
+ _TMDidFinishSetup.cold.1
+ _TMGetReferenceTimeAsync
+ _TMStartPeerClient
+ _TMStartPeerClient.cold.1
+ _TMStartPeerServer
+ _TMStartPeerServer.cold.1
+ ___TMGetReferenceTimeAsync_block_invoke
+ ___TMGetReferenceTimeAsync_block_invoke_2
+ ___block_descriptor_56_e8_32o40o48b_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s48l8s40l8
+ ___block_literal_global.141
+ ___block_literal_global.264
+ ___block_literal_global.267
+ ___block_literal_global.270
+ ___block_literal_global.95
- GCC_except_table28
- GCC_except_table35
- _TMSourceLocationBorder
- ___block_literal_global.143
- ___block_literal_global.266
- ___block_literal_global.269
- ___block_literal_global.274
- ___block_literal_global.90
- _kSourceLocationBorder
CStrings:
+ "TMAutoSetTimeNotification"
+ "TMDidFinishSetupCommand"
+ "TMGetReferenceTimeAsync"
+ "TMReferenceTimeSuccessful"
+ "TMStartPeerClientCommand"
+ "TMStartPeerServerCommand"
+ "void TMDidFinishSetup(void)"
+ "void TMStartPeerClient(void)"
+ "void TMStartPeerServer(void)"
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@16@24"
- "@56@0:8d16d24d32d40@48"
- "@64@0:8q16d24q32d40d48@56"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "ConvenienceConversions"
- "LocationBorder"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "T@\"NSString\",C,N,V_source"
- "T@\"NSString\",C,V_olsonName"
- "T@\"NSString\",C,V_source"
- "TB,N,GisSynthesized,V_synthesized"
- "TB,N,V_reliability"
- "TB,R"
- "TMTime"
- "Td,N"
- "Td,N,V_sf"
- "Td,N,V_sfUnc"
- "Td,N,V_utcUnc_s"
- "Tq,N,V_rtc_ns"
- "Tq,N,V_utc_ns"
- "UTF8String"
- "XPCConversions"
- "_olsonName"
- "_reliability"
- "_rtc_ns"
- "_sf"
- "_sfUnc"
- "_source"
- "_synthesized"
- "_utcUnc_s"
- "_utc_ns"
- "copy"
- "copyWithZone:"
- "currentHandler"
- "d"
- "d16@0:8"
- "d24@0:8d16"
- "dealloc"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeInt64ForKey:"
- "decodeObjectOfClass:forKey:"
- "description"
- "dictionary"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInt64:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "getValue:"
- "handleFailureInFunction:file:lineNumber:description:"
- "hasSameOlsonNameAs:"
- "init"
- "initWithCoder:"
- "initWithDictionary:"
- "initWithOlsonName:fromSource:"
- "initWithUtc_ns:utcUnc_s:rtc_ns:sf:sfUnc:source:"
- "isEqualToString:"
- "isEquivalent:"
- "isSynthesized"
- "numberWithBool:"
- "numberWithDouble:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "olsonName"
- "propagatedTimeAtRTC:"
- "propagatedUncertaintyAtRTC:"
- "q"
- "q16@0:8"
- "removeAllObjects"
- "removeObjectForKey:"
- "rtc_s"
- "setObject:forKey:"
- "setOlsonName:"
- "setReliability:"
- "setRtc_ns:"
- "setRtc_s:"
- "setSf:"
- "setSfUnc:"
- "setSource:"
- "setSynthesized:"
- "setUtcUnc_s:"
- "setUtc_ns:"
- "setUtc_s:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "supportsSecureCoding"
- "timeWithDictionary:"
- "timeWithUtc_s:utcUnc_s:rtc_s:sf:source:"
- "timeZoneWithOlsonName:fromSource:"
- "unsignedIntegerValue"
- "utc_s"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v24@0:8q16"
- "value:withObjCType:"

```
