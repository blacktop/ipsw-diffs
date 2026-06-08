## dmd

> `/usr/libexec/dmd`

```diff

-249.100.1.0.0
-  __TEXT.__text: 0x8a558
-  __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_stubs: 0xe9c0
-  __TEXT.__objc_methlist: 0x7fc4
-  __TEXT.__const: 0x170
-  __TEXT.__objc_classname: 0x1e74
-  __TEXT.__objc_methname: 0x118a7
+258.0.0.0.0
+  __TEXT.__text: 0x81624
+  __TEXT.__auth_stubs: 0xef0
+  __TEXT.__objc_stubs: 0xe940
+  __TEXT.__objc_methlist: 0x7fdc
+  __TEXT.__const: 0x168
+  __TEXT.__objc_classname: 0x1e43
+  __TEXT.__objc_methname: 0x1182a
   __TEXT.__objc_methtype: 0x1d98
-  __TEXT.__cstring: 0x539a
-  __TEXT.__oslogstring: 0xb1cb
-  __TEXT.__gcc_except_tab: 0x11c4
+  __TEXT.__cstring: 0x5489
+  __TEXT.__oslogstring: 0xb22e
+  __TEXT.__gcc_except_tab: 0x10bc
   __TEXT.__ustring: 0x80a
   __TEXT.__dlopen_cstrs: 0xaf
-  __TEXT.__unwind_info: 0x2528
-  __DATA_CONST.__auth_got: 0x758
-  __DATA_CONST.__got: 0x1338
-  __DATA_CONST.__const: 0x2748
-  __DATA_CONST.__cfstring: 0x57a0
+  __TEXT.__unwind_info: 0x2210
+  __DATA_CONST.__const: 0x2740
+  __DATA_CONST.__cfstring: 0x57e0
   __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x618
-  __DATA_CONST.__objc_arraydata: 0x508
-  __DATA_CONST.__objc_arrayobj: 0x960
+  __DATA_CONST.__objc_arraydata: 0x530
+  __DATA_CONST.__objc_arrayobj: 0x978
   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0x788
+  __DATA_CONST.__got: 0x1338
   __DATA.__objc_const: 0x1d6e8
-  __DATA.__objc_selrefs: 0x41a8
+  __DATA.__objc_selrefs: 0x4190
   __DATA.__objc_ivar: 0x430
   __DATA.__objc_data: 0x45b0
   __DATA.__data: 0xc60
-  __DATA.__bss: 0x4e8
+  __DATA.__bss: 0x4f8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: 8AD9366A-FA41-3562-97E4-3F6354F2BA4E
-  Functions: 3235
-  Symbols:   912
-  CStrings:  5307
+  UUID: 44DFFF43-7A92-34FE-A337-0F2094E183BE
+  Functions: 3218
+  Symbols:   918
+  CStrings:  5311
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_retain_x9
CStrings:
+ "%{public}@: Newer declaration of type %{public}@ found. Removing old one from DB to skip uninstall"
+ "(%K != nil) AND (%K == %@) AND (%K == %@) AND (%K == %@)"
+ "(%K != nil) AND (NOT (%K IN %@)) AND (%K == %@) AND (%K == %@) AND (%K == %@)"
+ "(%K == nil) AND (%K == %@) AND (%K == %@) AND (%K == %@)"
+ "(%K IN %@) AND (%K == %@) AND (%K == %@) AND (%K == %@)"
+ "Error fetching orphaned policies for declaration %{public}@: %{public}@"
+ "Pruning orphaned policy of type %{public}@ identifier %{public}@ (no longer in declaration %{public}@)"
+ "ScreenTimeSettings"
+ "eureka"
+ "isSkipUninstallOnSupersedeType:"
+ "typesSkippingUninstallOnSupersede"
- "(%K == nil) AND (%K == %@) AND (%K == %@)"
- "(%K IN %@) AND (%K == %@) AND (%K == %@)"
- "Failed to set bundle identifiers %{public}@ for personaID %{public}@ with error: %{public}@"
- "Newer app exceptions declaration found. Removing old one from DB to skip uninstall"
- "getFileSystemRepresentation:maxLength:"
- "listAllPersonaWithAttributes"
- "setBundlesIdentifiers:forPersonaWithPersonaUniqueString:completionHandler:"
- "userPersonaBundleIDList"
- "userPersonaUniqueString"

```
