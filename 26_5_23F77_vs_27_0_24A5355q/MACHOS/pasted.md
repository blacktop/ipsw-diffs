## pasted

> `/System/Library/PrivateFrameworks/Pasteboard.framework/Support/pasted`

```diff

-9126.4.22.0.0
-  __TEXT.__text: 0x1d1a0
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0x43a0
-  __TEXT.__objc_methlist: 0x1378
+9127.0.66.0.0
+  __TEXT.__text: 0x1c8e0
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__objc_stubs: 0x44a0
+  __TEXT.__objc_methlist: 0x13b0
   __TEXT.__const: 0x198
-  __TEXT.__objc_methname: 0x4e4c
-  __TEXT.__objc_classname: 0x53a
-  __TEXT.__objc_methtype: 0xd2b
-  __TEXT.__cstring: 0x1c46
-  __TEXT.__oslogstring: 0x1d07
-  __TEXT.__gcc_except_tab: 0x790
+  __TEXT.__objc_methname: 0x4fdf
+  __TEXT.__objc_classname: 0x520
+  __TEXT.__cstring: 0x1c8e
+  __TEXT.__objc_methtype: 0xd76
+  __TEXT.__oslogstring: 0x21bc
+  __TEXT.__gcc_except_tab: 0x768
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0x770
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x468
-  __DATA_CONST.__const: 0x13b0
-  __DATA_CONST.__cfstring: 0x18a0
+  __TEXT.__unwind_info: 0x700
+  __DATA_CONST.__const: 0x13d8
+  __DATA_CONST.__cfstring: 0x18c0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xd0
-  __DATA_CONST.__objc_arraydata: 0xe0
+  __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x2e48
-  __DATA.__objc_selrefs: 0x1300
-  __DATA.__objc_ivar: 0x170
+  __DATA_CONST.__auth_got: 0x6c8
+  __DATA_CONST.__got: 0x480
+  __DATA.__objc_const: 0x2e80
+  __DATA.__objc_selrefs: 0x1348
+  __DATA.__objc_ivar: 0x174
   __DATA.__objc_data: 0xa50
   __DATA.__data: 0x4e8
   __DATA.__thread_vars: 0x30
   __DATA.__thread_data: 0x8
   __DATA.__thread_bss: 0x8
-  __DATA.__bss: 0x1a9
+  __DATA.__bss: 0x1b0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BB5302B3-EFD7-381C-A26C-18ACB88B1153
-  Functions: 507
-  Symbols:   359
-  CStrings:  1523
+  UUID: A2F9D97B-B427-392D-A27E-49E85AC105BC
+  Functions: 513
+  Symbols:   371
+  CStrings:  1553
 
Symbols:
+ _OBJC_CLASS_$_NSFileWrapper
+ _OBJC_CLASS_$_UTType
+ _PBTemporaryFolderURL
+ _UTTypeDirectory
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x9
CStrings:
+ "Authorization for %@ (pid %d) on pasteboard %@ recorded successfully."
+ "Bundle ID %@ from team %@ is not allowed to preauthorize paste."
+ "Bundle ID %@ is authorizing paste on pasteboard %@ for bundle ID %@ (pid %d) at changeCount %ld."
+ "Failed to reconstruct directory from serialized NSFileWrapper: %@"
+ "Failed to retrieve pasteboard %@ for authorization: %@"
+ "Invalid audit token data length from %@."
+ "PBItem _saveRepresentationsToBaseURL: data load completion fired item=%@ type=%{public}@ data=%lu bytes error=%{public}@"
+ "PBItem _saveRepresentationsToBaseURL: requesting data load item=%@ type=%{public}@ rep=%p"
+ "Pasteboard changeCount mismatch: expected %ld, got %ld. Pasteboard content has changed."
+ "Reconstructed directory from serialized NSFileWrapper at %@"
+ "TB,N,GisAllowedToPreauthorizePaste,V_allowedToPreauthorizePaste"
+ "_allowedToPreauthorizePaste"
+ "allowedToPreauthorizePaste"
+ "com.apple.Pasteboard.proxy-paste-authorization"
+ "conformsToType:"
+ "getBytes:length:"
+ "initWithSerializedRepresentation:"
+ "isAllowedToPreauthorizePaste"
+ "isDirectory"
+ "preauthorizePasteForAuditTokenData:pasteboardName:changeCount:completionBlock:"
+ "serializeToBaseURL: _serializeItemRepresentations completion fired for pasteboard=%{public}@ error=%{public}@"
+ "serializeToBaseURL: about to wait on semaphore for pasteboard=%{public}@ itemCollection=%@ (waiting for source data-load replies)"
+ "serializeToBaseURL: semaphore signaled for pasteboard=%{public}@ itemCollection=%@ error=%{public}@"
+ "serializeToBaseURL: starting _serializeItemRepresentations for pasteboard=%{public}@ itemCollection=%@ items=%lu"
+ "setAllowedToPreauthorizePaste:"
+ "typeWithIdentifier:"
+ "v48@0:8@\"NSData\"16@\"NSString\"24q32@?<v@?@\"NSError\">40"
+ "v48@0:8@16@24q32@?40"
+ "writeToURL:options:originalContentsURL:error:"

```
