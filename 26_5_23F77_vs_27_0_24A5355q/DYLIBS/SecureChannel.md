## SecureChannel

> `/System/Library/PrivateFrameworks/SecureChannel.framework/SecureChannel`

```diff

 1.0.67.0.0
-  __TEXT.__text: 0x89c
-  __TEXT.__auth_stubs: 0x140
+  __TEXT.__text: 0x884
   __TEXT.__objc_methlist: 0x148
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0xad
+  __TEXT.__cstring: 0xb1
   __TEXT.__unwind_info: 0xa8
-  __TEXT.__objc_classname: 0x77
-  __TEXT.__objc_methname: 0x285
-  __TEXT.__objc_methtype: 0x13b
-  __TEXT.__objc_stubs: 0x1e0
-  __DATA_CONST.__got: 0x30
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xa8
+  __DATA_CONST.__got: 0x30
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x338
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0x120

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9677AA36-D586-363A-A2CA-662C53CAF4F4
+  UUID: 60178D3A-E70E-3FC6-95C8-4F43A2477E02
   Functions: 23
-  Symbols:   143
-  CStrings:  73
+  Symbols:   146
+  CStrings:  17
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x24
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
- _objc_autoreleaseReturnValue
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
Functions:
~ +[SecureChannelController actionForURL:completion:] : 268 -> 264
~ ___51+[SecureChannelController actionForURL:completion:]_block_invoke : 132 -> 136
~ +[SecureChannelServiceProxy sharedInstance] : 84 -> 68
~ -[SecureChannelServiceProxy init] : 204 -> 200
~ -[SecureChannelAction initWithURL:title:message:] : 172 -> 188
~ -[SecureChannelAction encodeWithCoder:] : 136 -> 128
~ -[SecureChannelAction initWithCoder:] : 252 -> 240
CStrings:
- ".cxx_destruct"
- "@\"NSObject<SecureChannelService>\""
- "@\"NSString\""
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@40@0:8@16@24@32"
- "B16@0:8"
- "NSCoding"
- "NSSecureCoding"
- "SecureChannelAction"
- "SecureChannelController"
- "SecureChannelService"
- "SecureChannelServiceProxy"
- "T@\"NSString\",R,C,N,V_message"
- "T@\"NSString\",R,C,N,V_title"
- "T@\"NSURL\",R,C,N,V_url"
- "TB,R"
- "_connectionToService"
- "_message"
- "_remoteObject"
- "_title"
- "_url"
- "absoluteString"
- "actionForURL:completion:"
- "decodeObjectOfClass:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "hasPrefix:"
- "init"
- "initWithCoder:"
- "initWithMachServiceName:options:"
- "initWithURL:title:message:"
- "interfaceWithProtocol:"
- "performWithCompletionHandler:"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "runApproverFlowForURL:completion:"
- "runApproverFlowForURL:withCompletion:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "sharedInstance"
- "supportsSecureCoding"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"SecureChannelAction\"@\"NSError\">24"
- "v32@0:8@16@?24"

```
