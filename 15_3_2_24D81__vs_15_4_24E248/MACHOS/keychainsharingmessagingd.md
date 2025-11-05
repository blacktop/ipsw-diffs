## keychainsharingmessagingd

> `/usr/libexec/keychainsharingmessagingd`

```diff

-61439.81.1.0.0
-  __TEXT.__text: 0x18cb0
-  __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_stubs: 0x120
-  __TEXT.__objc_methlist: 0x1d8
-  __TEXT.__cstring: 0xa6b
-  __TEXT.__objc_methname: 0xe4d
-  __TEXT.__const: 0x3e0
+61439.101.1.0.0
+  __TEXT.__text: 0x1898c
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__objc_methlist: 0x434
+  __TEXT.__const: 0x380
+  __TEXT.__cstring: 0x75e
+  __TEXT.__objc_methname: 0xc8f
   __TEXT.__constg_swiftt: 0x25c
   __TEXT.__swift5_typeref: 0x410
   __TEXT.__swift5_reflstr: 0x102
   __TEXT.__swift5_fieldmd: 0x184
   __TEXT.__swift5_capture: 0x264
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__objc_classname: 0xb5
-  __TEXT.__objc_methtype: 0xa8f
+  __TEXT.__objc_classname: 0x86
+  __TEXT.__objc_methtype: 0xa0e
+  __TEXT.__swift_as_entry: 0x5c
+  __TEXT.__swift_as_ret: 0x48
   __TEXT.__oslogstring: 0xa3a
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x618
-  __TEXT.__eh_frame: 0xd88
-  __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x1d0
+  __TEXT.__unwind_info: 0x5d0
+  __TEXT.__eh_frame: 0xdb0
+  __DATA_CONST.__auth_got: 0x640
+  __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__auth_ptr: 0x168
   __DATA_CONST.__const: 0x7a0
-  __DATA_CONST.__cfstring: 0xe0
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xe00
-  __DATA.__objc_selrefs: 0x220
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__objc_data: 0x468
-  __DATA.__data: 0x880
+  __DATA.__objc_const: 0x570
+  __DATA.__objc_selrefs: 0x360
+  __DATA.__objc_data: 0x418
+  __DATA.__data: 0x730
   __DATA.__common: 0x48
   __DATA.__bss: 0x400
-  - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: CD6F5114-DBC1-3D6C-B5DB-CA9DC78A432F
-  Functions: 388
-  Symbols:   335
-  CStrings:  347
+  UUID: 6B296D86-3638-3043-83D5-C0214C66211C
+  Functions: 358
+  Symbols:   323
+  CStrings:  284
 
Symbols:
+ _OBJC_CLASS_$_KCSharingGroupInvite
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSString
- _OBJC_CLASS_$_NSURL
- ___CFConstantStringClassReference
- _objc_opt_class
- _objc_setProperty_nonatomic_copy
- _objc_storeStrong
CStrings:
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSString\""
- "@\"NSURL\""
- "@24@0:8@\"NSCoder\"16"
- "@72@0:8@16@24@32@40@48@56@64"
- "Insufficient space allocated to copy string contents"
- "KCSharingGroupInvite"
- "NSCoding"
- "NSSecureCoding"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"NSData\",R,C,N,V_inviteToken"
- "T@\"NSDate\",R,C,N,V_sentTime"
- "T@\"NSString\",C,N,V_displayName"
- "T@\"NSString\",R,C,N,V_groupID"
- "T@\"NSString\",R,C,N,V_inviteeHandle"
- "T@\"NSString\",R,C,N,V_senderHandle"
- "T@\"NSURL\",R,C,N,V_shareURL"
- "TB,R"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_displayName"
- "_groupID"
- "_inviteToken"
- "_inviteeHandle"
- "_senderHandle"
- "_sentTime"
- "_shareURL"
- "decodeObjectOfClass:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "invalid Collection: less than 'count' elements in collection"
- "inviteToken"
- "inviteeHandle"
- "senderHandle"
- "setDisplayName:"
- "supportsSecureCoding"
- "v24@0:8@\"NSCoder\"16"

```
