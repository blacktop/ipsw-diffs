## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-1968.300.31.0.0
-  __TEXT.__text: 0x14565c
+1968.400.1.0.0
+  __TEXT.__text: 0x1465a8
   __TEXT.__auth_stubs: 0x1cf0
-  __TEXT.__objc_methlist: 0xd18c
+  __TEXT.__objc_methlist: 0xd22c
   __TEXT.__const: 0x422
   __TEXT.__gcc_except_tab: 0x47dc
-  __TEXT.__oslogstring: 0x19f41
-  __TEXT.__cstring: 0x1062b
+  __TEXT.__oslogstring: 0x1a107
+  __TEXT.__cstring: 0x1073b
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
   __TEXT.__swift5_typeref: 0x8
-  __TEXT.__unwind_info: 0x4f08
-  __TEXT.__objc_classname: 0x19d1
-  __TEXT.__objc_methname: 0x20045
-  __TEXT.__objc_methtype: 0x7973
-  __TEXT.__objc_stubs: 0x14260
-  __DATA_CONST.__got: 0x12a8
-  __DATA_CONST.__const: 0x5288
+  __TEXT.__unwind_info: 0x4f30
+  __TEXT.__objc_classname: 0x19e4
+  __TEXT.__objc_methname: 0x200fb
+  __TEXT.__objc_methtype: 0x7ac2
+  __TEXT.__objc_stubs: 0x14300
+  __DATA_CONST.__got: 0x12c0
+  __DATA_CONST.__const: 0x52b0
   __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x218
+  __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68d0
+  __DATA_CONST.__objc_selrefs: 0x68e0
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x460
   __AUTH_CONST.__auth_got: 0xe88
   __AUTH_CONST.__const: 0x1b20
   __AUTH_CONST.__cfstring: 0x73e0
-  __AUTH_CONST.__objc_const: 0x3b0d8
-  __AUTH_CONST.__objc_intobj: 0x540
+  __AUTH_CONST.__objc_const: 0x3b408
+  __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1a90
-  __DATA.__objc_ivar: 0xd70
-  __DATA.__data: 0x1958
+  __DATA.__objc_ivar: 0xd74
+  __DATA.__data: 0x19b8
   __DATA.__bss: 0x1b60
   __DATA_DIRTY.__objc_data: 0x1d10
   __DATA_DIRTY.__bss: 0x388

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 79F1C171-0AB9-3596-BB38-E1F02D9DE19A
-  Functions: 6560
-  Symbols:   1579
-  CStrings:  10111
+  UUID: F75FC882-FEF0-34A4-A4AB-CFF15F90284A
+  Functions: 6572
+  Symbols:   1582
+  CStrings:  10133
 
Symbols:
+ _IDSLocalNetworkHandshakeContextKey
+ _IDSSessionDisallowHandshakeOverQRKey
+ _IDSSessionLocalNetworkHandshakeKey
CStrings:
+ "%@: IDSSessionLocalNetworkHandshakeKey is NOT present"
+ "%@: IDSSessionLocalNetworkHandshakeKey is present: %@"
+ "-[_IDSConnection didReceiveLocalNetworkHandshake:handshakeSucceeded:forTopic:sessionID:toIdentifier:fromID:error:]"
+ "-[_IDSService beginLocalNetworkHandshakeFromAccount:destinations:options:]"
+ "-[_IDSService connection:account:didReceiveLocalNetworkHandshake:fromID:context:]"
+ "@\"IDSSession\""
+ "Handshake invitation succeeded %@ fromID %@"
+ "IDSSessionDelegate"
+ "Incoming handshake invitation %@ forTopic %@ sessionID %@ toIdentifier %@ fromID %@ succeeded %@"
+ "_handshakeSession"
+ "beginLocalNetworkHandshakeFromAccount {account: %@}"
+ "beginLocalNetworkHandshakeFromAccount {with data: %lu}"
+ "beginLocalNetworkHandshakeFromAccount: IDSLocalNetworkHandshakeContextKey value is not NSData: %@"
+ "connection:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "didReceiveLocalNetworkHandshake:handshakeSucceeded:forTopic:sessionID:toIdentifier:fromID:error:"
+ "v24@0:8@\"IDSSession\"16"
+ "v32@0:8@\"IDSSession\"16@\"NSArray\"24"
+ "v32@0:8@\"IDSSession\"16@\"NSString\"24"
+ "v36@0:8@\"IDSSession\"16I24@\"NSError\"28"
+ "v52@0:8@\"IDSConnection\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v68@0:8@\"NSDictionary\"16B24@\"NSString\"28@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSError\"60"
+ "v68@0:8@16B24@28@36@44@52@60"

```
