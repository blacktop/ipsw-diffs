## DumpPanic

> `/usr/libexec/DumpPanic`

```diff

-274.0.0.0.0
-  __TEXT.__text: 0x22784
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_stubs: 0x1ae0
-  __TEXT.__objc_methlist: 0x4fc
+278.0.0.0.0
+  __TEXT.__text: 0x241f0
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__objc_stubs: 0x1be0
+  __TEXT.__objc_methlist: 0x538
   __TEXT.__const: 0x2ee
-  __TEXT.__cstring: 0x2444
-  __TEXT.__gcc_except_tab: 0x844
-  __TEXT.__oslogstring: 0x3b4f
+  __TEXT.__cstring: 0x24ab
+  __TEXT.__gcc_except_tab: 0x764
+  __TEXT.__oslogstring: 0x3de5
   __TEXT.__ustring: 0x1c6
-  __TEXT.__objc_classname: 0xc7
-  __TEXT.__objc_methname: 0x14dd
-  __TEXT.__objc_methtype: 0x3f7
-  __TEXT.__unwind_info: 0x5c4
-  __DATA_CONST.__auth_got: 0x658
+  __TEXT.__objc_classname: 0xdd
+  __TEXT.__objc_methname: 0x15c9
+  __TEXT.__objc_methtype: 0x465
+  __TEXT.__unwind_info: 0x5dc
+  __DATA_CONST.__auth_got: 0x660
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x788
-  __DATA_CONST.__cfstring: 0x23c0
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__const: 0x7e8
+  __DATA_CONST.__cfstring: 0x2440
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x178
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA.__objc_const: 0xb58
-  __DATA.__objc_selrefs: 0x710
-  __DATA.__objc_classrefs: 0x140
-  __DATA.__objc_superrefs: 0x18
-  __DATA.__objc_ivar: 0x90
-  __DATA.__objc_data: 0x370
+  __DATA.__objc_const: 0xc50
+  __DATA.__objc_selrefs: 0x750
+  __DATA.__objc_classrefs: 0x148
+  __DATA.__objc_superrefs: 0x20
+  __DATA.__objc_ivar: 0x9c
+  __DATA.__objc_data: 0x3c0
   __DATA.__data: 0xf0
   __DATA.__bss: 0x9f0
   __INFO_FILTER.__disable: 0x0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5CC1411E-EB8D-358C-8617-C14B7962463E
-  Functions: 466
-  Symbols:   277
-  CStrings:  1317
+  UUID: 25E9A2FB-382A-3440-AF1C-5AC70A079B30
+  Functions: 472
+  Symbols:   278
+  CStrings:  1361
 
Symbols:
+ _asprintf
+ _objc_unsafeClaimAutoreleasedReturnValue
- _objc_retain_x9
CStrings:
+ "\x12"
+ "%@ left in pull in list"
+ "%@.%s%@.core.gz"
+ "%s core already compressed, skipping collection"
+ "%s core is empty"
+ "%s/%@"
+ "%s/staged"
+ "/private/var/mobile/Library/Logs/CrashReporter/Panics/staged"
+ "/private/var/mobile/Library/Logs/CrashReporter/Panics/staged/tempUserSpaceCore.XXX"
+ "/staged"
+ "@24@0:8d16"
+ "@32@0:8r*16r*24"
+ "Cannot find %@"
+ "Cannot move staged '%{public}@' to panics folder : %{public}@"
+ "Detected stress rack device, setting xattr on original %s core"
+ "Failed to allocate compression buffer for %s core"
+ "Failed to close compressed %s core with error : %d"
+ "Failed to close compressed %s core with error : %s"
+ "Failed to open %s core compressed output file with error %s"
+ "Failed to read content from %s core"
+ "Failed to rename compressed %s from %s to %s"
+ "Failed to set %s xattr returned error : %s"
+ "Finished processing %@ core, avaiable at %@"
+ "Found %lu sets of %@ corefiles (policy limit %u, %lu set staged), not cleaning up"
+ "Found %lu sets of corefiles (policy limit %u, %lu set staged), not cleaning up"
+ "Found %lu sets of cores under staged folder"
+ "Found %s core at %s"
+ "Moved staged '%{public}@ to panics folder"
+ "Neither can find %@"
+ "No %s core found at %s"
+ "Prune %@ core files in %@"
+ "Prune core files in %@"
+ "Removing original %s core"
+ "Removing prior %@ corefiles, found %lu sets (policy limit %u)"
+ "Removing prior %@ corefiles, found %lu sets (policy limit %u, %lu set staged)"
+ "Removing prior corefiles, found %lu sets (policy limit %u, %lu set staged)"
+ "UserCoreFileHandler"
+ "UserSpaceCoreCompressed"
+ "^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}"
+ "_input_core"
+ "_input_corefile_name"
+ "_input_corefile_path"
+ "allValues"
+ "failed to allocate staging directory string"
+ "failed to setup corefile stage directory due to error: %s"
+ "failed to setup corefile stage directory with error: %s"
+ "found timestamp %@"
+ "gzopen %s"
+ "gzwrite failed to write %s core"
+ "initWithCoreFilePath::"
+ "lastPathComponent"
+ "launchd"
+ "moveItemAtPath:toPath:error:"
+ "open %s failed with error: %s"
+ "ready to submit %s"
+ "removeObjectForKey:"
+ "removeObjectsInArray:"
+ "replaceObjectAtIndex:withObject:"
+ "saveUserSpaceCoreToDisk:"
+ "saved core file %@"
+ "staged"
- "%s/%@.%slaunchd.core.gz"
- "/private/var/mobile/Library/Logs/CrashReporter/Panics/tempLaunchdCore.XXX"
- "Detected stress rack device, setting xattr on original launchd core"
- "Failed to allocate compression buffer for launchd core"
- "Failed to close compressed launchd core with error : %d"
- "Failed to close compressed launchd core with error : %s"
- "Failed to open launchd-core compressed output file with error %s"
- "Failed to read content from launchd core"
- "Failed to rename compressed launchd core from %s to %s"
- "Failed to set %s xattr on %s"
- "Finished processing launchd corefile, avaiable at %@"
- "Found %lu sets of corefiles (policy limit %u), not cleaning up"
- "Found launchd corefile"
- "LaunchdCoreCompressed"
- "No launchd debug core found at %s"
- "No launchd development core found at %s, looking for debug..."
- "Removing original launchd core"
- "gzwrite failed to write launchd core"
- "launchd core already compressed, skipping collection"
- "launchd core is empty"
- "open %s failed with error : %s"

```
