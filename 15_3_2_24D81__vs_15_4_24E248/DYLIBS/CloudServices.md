## CloudServices

> `/System/Library/PrivateFrameworks/CloudServices.framework/Versions/A/CloudServices`

```diff

-638.80.3.0.0
-  __TEXT.__text: 0x28e40
-  __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_methlist: 0x1b2c
+638.100.48.0.0
+  __TEXT.__text: 0x29340
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_methlist: 0x1f18
   __TEXT.__const: 0xc90
-  __TEXT.__cstring: 0x21ad
-  __TEXT.__gcc_except_tab: 0x5b4
+  __TEXT.__cstring: 0x21f4
+  __TEXT.__gcc_except_tab: 0x67c
   __TEXT.__oslogstring: 0x20af
-  __TEXT.__unwind_info: 0x860
+  __TEXT.__unwind_info: 0x890
   __TEXT.__objc_classname: 0x298
-  __TEXT.__objc_methname: 0x46e5
-  __TEXT.__objc_methtype: 0xcef
+  __TEXT.__objc_methname: 0x482a
+  __TEXT.__objc_methtype: 0xe08
   __TEXT.__objc_stubs: 0x3160
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x5a0
+  __DATA_CONST.__const: 0x5d8
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11a0
+  __DATA_CONST.__objc_selrefs: 0x1240
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x450
-  __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x2260
-  __AUTH_CONST.__objc_const: 0x3330
+  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__const: 0x6b0
+  __AUTH_CONST.__cfstring: 0x2200
+  __AUTH_CONST.__objc_const: 0x2c40
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x5f0

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1918D010-5E51-3A41-BB54-237D486A0E9F
-  Functions: 942
-  Symbols:   425
-  CStrings:  1788
+  UUID: 5F2668F8-9D04-3FBB-9034-C701B7D9326F
+  Functions: 956
+  Symbols:   423
+  CStrings:  1792
 
Symbols:
- _ccrsa_ctx_public
- _ccrsa_generate_fips186_key
CStrings:
+ "-[SecureBackup recoverSilentWithCDPContext:allRecords:altDSID:flowID:deviceSessionID:error:]"
+ "-[SecureBackup recoverWithCDPContext:escrowRecord:altDSID:flowID:deviceSessionID:error:]"
+ "@64@0:8@16@24@32@40@48^@56"
+ "Unknown federation %@"
+ "intValue"
+ "recoverSilentWithCDPContext:allRecords:altDSID:flowID:deviceSessionID:error:"
+ "recoverSilentWithCDPContextInDaemon:allRecords:altDSID:flowID:deviceSessionID:reply:"
+ "recoverWithCDPContext:escrowRecord:altDSID:flowID:deviceSessionID:error:"
+ "recoverWithCDPContextInDaemon:escrowRecord:altDSID:flowID:deviceSessionID:reply:"
+ "secure terms needed for %@"
+ "v64@0:8@\"OTICDPRecordContext\"16@\"NSArray\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"NSDictionary\"@\"NSError\">56"
+ "v64@0:8@\"OTICDPRecordContext\"16@\"OTEscrowRecord\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"NSDictionary\"@\"NSError\">56"
+ "v64@0:8@16@24@32@40@48@?56"
- "B32@0:8@16@24"
- "Could not generate key: %d"
- "Error decoding recovery record"
- "Escrow error encrypting data (spare)"
- "Local SRP verify failed"
- "could not create local SRP recovery blob"

```
