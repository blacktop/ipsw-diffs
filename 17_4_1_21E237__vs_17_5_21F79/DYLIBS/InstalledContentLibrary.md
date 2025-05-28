## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

```diff

-1270.102.7.0.0
-  __TEXT.__text: 0xa1088
-  __TEXT.__auth_stubs: 0x1310
+1270.120.9.0.0
+  __TEXT.__text: 0xa146c
+  __TEXT.__auth_stubs: 0x1320
   __TEXT.__objc_methlist: 0x4360
   __TEXT.__const: 0xf8a0
   __TEXT.__gcc_except_tab: 0x97c
-  __TEXT.__cstring: 0x156d0
+  __TEXT.__cstring: 0x157c2
   __TEXT.__dlopen_cstrs: 0x111
   __TEXT.__oslogstring: 0x8b6
-  __TEXT.__unwind_info: 0x21c8
+  __TEXT.__unwind_info: 0x21e4
   __TEXT.__eh_frame: 0xe30
   __TEXT.__objc_classname: 0x566
-  __TEXT.__objc_methname: 0xcc41
+  __TEXT.__objc_methname: 0xcc47
   __TEXT.__objc_methtype: 0x169a
   __TEXT.__objc_stubs: 0x80e0
   __DATA_CONST.__got: 0x1a8

   __DATA_CONST.__objc_classrefs: 0x270
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x978
-  __AUTH_CONST.__cfstring: 0xbe40
+  __AUTH_CONST.__cfstring: 0xbea0
   __AUTH_CONST.__objc_const: 0x1c88
   __AUTH_CONST.__const: 0x56e8
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__objc_dictobj: 0x11a8
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__auth_got: 0x998
+  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__auth_got: 0x9a0
   __DATA.__objc_ivar: 0x4f4
   __DATA.__data: 0x1178
   __DATA.__bss: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1809
-  Symbols:   6245
-  CStrings:  4185
+  Functions: 1812
+  Symbols:   6250
+  CStrings:  4189
 
Symbols:
+ _MILoadInfoPlistWithError
+ _MILoadRawInfoPlist
+ __CFBundleCopyInfoPlistURL
+ __CreateCFBundle
+ ___block_literal_global.105
+ _objc_msgSend$setObject:forKey:
- ___block_literal_global.121
- _objc_msgSend$synchronize
CStrings:
+ "CFBundleGetInfoDictionary failed for bundle at %@"
+ "Container for identifier %@ is not a data container; found class %ld."
+ "Error when introspecting %@"
+ "Expected Info.plist file at %@ but found something that was not a file."
+ "ExtensionDataContainerParentIDUpdateVersion"
+ "Failed to create CFBundle for %@"
+ "Failed to delete partially created container %@ : %@"
+ "Failed to find container of class %llu with identity %@/%@"
+ "Failed to get Info.plist URL from %@; falling back to assumed path"
+ "MILoadInfoPlistWithError"
+ "Removing created container for which we were unable to create an object to represent: %@"
+ "_CreateCFBundle"
+ "setObject:forKey:"
- "CFBundleGetInfoDictionary failed for bundle %@"
- "Container (%ld) for identifier %@ is not a data container."
- "Error when introspecting %@ : %@"
- "Expected Info.plist file at %@ but found something else: %@"
- "Failed to create CFBundle from URL %@"
- "Failed to find container of class %llu with identifier %@"
- "MILoadInfoPlist"
- "UpdatedPluginContainersWithParentIDWithSafeHarborFix"
- "synchronize"

```
