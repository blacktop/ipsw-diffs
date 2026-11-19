## com.apple.MobileAsset.DownloadService.Builtin

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/Versions/A/XPCServices/com.apple.MobileAsset.DownloadService.Builtin.xpc/Contents/MacOS/com.apple.MobileAsset.DownloadService.Builtin`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2215.0.20.0.0
-  __TEXT.__text: 0x214d0
+2215.41.2.0.0
+  __TEXT.__text: 0x21c5c
   __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_stubs: 0x3f60
-  __TEXT.__objc_methlist: 0x1bfc
+  __TEXT.__objc_stubs: 0x3fa0
+  __TEXT.__objc_methlist: 0x1c2c
   __TEXT.__const: 0x6ac
-  __TEXT.__cstring: 0x447e
-  __TEXT.__gcc_except_tab: 0x1110
-  __TEXT.__objc_methname: 0x5739
-  __TEXT.__oslogstring: 0x5ae9
+  __TEXT.__cstring: 0x4671
+  __TEXT.__gcc_except_tab: 0x1160
+  __TEXT.__objc_methname: 0x5818
+  __TEXT.__oslogstring: 0x5c97
   __TEXT.__objc_classname: 0x29e
   __TEXT.__objc_methtype: 0x10b4
   __TEXT.__swift5_typeref: 0xda

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x8d0
+  __TEXT.__unwind_info: 0x8d8
   __TEXT.__eh_frame: 0xc4
   __DATA_CONST.__const: 0x880
-  __DATA_CONST.__cfstring: 0x2b00
+  __DATA_CONST.__cfstring: 0x2da0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__auth_got: 0x5e8
   __DATA_CONST.__got: 0x338
   __DATA_CONST.__auth_ptr: 0x160
-  __DATA.__objc_const: 0x2c98
-  __DATA.__objc_selrefs: 0x1370
-  __DATA.__objc_ivar: 0x230
+  __DATA.__objc_const: 0x2cc8
+  __DATA.__objc_selrefs: 0x1388
+  __DATA.__objc_ivar: 0x234
   __DATA.__objc_data: 0x518
   __DATA.__data: 0x5d8
   __DATA.__crash_info: 0x148

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 669
+  Functions: 673
   Symbols:   308
-  CStrings:  1847
+  CStrings:  1877
 
CStrings:
+ "AutoAuthorization"
+ "AutoConnectionObserver"
+ "AutoConnector"
+ "AutoControl-ConsiderRemoval"
+ "AutoControl-Eliminate"
+ "AutoControl-LookupGrant"
+ "AutoControl-OverflowTrim"
+ "AutoControl-Removal"
+ "AutoControl-SecureMonitor"
+ "AutoControl-SecureStartup"
+ "AutoControl-SecureUngraft"
+ "AutoJobCalculateDownloadSpace"
+ "AutoLookupCache"
+ "AutoSetStatus"
+ "Cancelling task due to failure to add it to activeDownload list | Identifier:%{public}@"
+ "Secure"
+ "Secure-Control"
+ "Secure-Control-Commit"
+ "Secure-Control-Exclave"
+ "Secure-Control-Graft"
+ "Secure-Control-LatestDownloaded"
+ "Secure-Control-LocalContentURL"
+ "Secure-Control-Personalize"
+ "Secure-Control-PersonalizeGraft"
+ "T@\"NSMutableDictionary\",&,V_serviceIdentifierToClientId"
+ "[MADownloadServiceBuiltin]: Attempting to start up builtin service built Oct  8 2026 00:20:06"
+ "[Manager]: Cancelling task due to failure to add it to active downloads | TaskDescriptor:%{public}@"
+ "[Manager]: Failed to extract taskDescriptor from description | TaskDescription:%{public}@"
+ "[Manager]: Failed to extract taskDescriptor from description(task not removed) | TaskDescription:%{public}@"
+ "[Manager]: Unable to determine taskDescriptor from description(no task returned) | TaskDescription:%{public}@"
+ "_serviceIdentifierToClientId"
+ "activeDownloadsKeyForEncodedTaskDescription:"
+ "extractOriginalTaskDescriptorFromEncodedTaskDescription:"
+ "serviceIdentifierToClientId"
+ "setServiceIdentifierToClientId:"
- "Failed to add task to activeDownload list | Identifier:%{public}@"
- "SecureControl"
- "SecureMA"
- "[MADownloadServiceBuiltin]: Attempting to start up builtin service built Aug  8 2026 21:05:10"
- "numberWithUnsignedLong:"
```
