## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

-316.0.0.0.0
-  __TEXT.__text: 0x1314c
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_stubs: 0x120
-  __TEXT.__cstring: 0x83d9
+320.0.0.0.0
+  __TEXT.__text: 0x14fec
+  __TEXT.__auth_stubs: 0x13f0
+  __TEXT.__objc_stubs: 0x580
+  __TEXT.__objc_methlist: 0x5c
+  __TEXT.__cstring: 0x8cf9
   __TEXT.__const: 0x688
+  __TEXT.__objc_methname: 0x3ff
+  __TEXT.__objc_classname: 0xc
+  __TEXT.__objc_methtype: 0x3a
   __TEXT.__gcc_except_tab: 0x110
-  __TEXT.__objc_methname: 0xd8
-  __TEXT.__unwind_info: 0x3a8
-  __DATA_CONST.__auth_got: 0x9c8
-  __DATA_CONST.__got: 0x130
+  __TEXT.__unwind_info: 0x3c8
+  __DATA_CONST.__auth_got: 0xa08
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x5e8
-  __DATA_CONST.__cfstring: 0xd40
+  __DATA_CONST.__const: 0x628
+  __DATA_CONST.__cfstring: 0x12e0
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x48
-  __DATA.__data: 0x510
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0xd0
+  __DATA.__objc_selrefs: 0x170
+  __DATA.__objc_ivar: 0x4
+  __DATA.__objc_data: 0x50
+  __DATA.__data: 0x520
   __DATA.__common: 0x11c
-  __DATA.__bss: 0x488
+  __DATA.__bss: 0x4b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 210
-  Symbols:   354
-  CStrings:  971
+  Functions: 222
+  Symbols:   369
+  CStrings:  1091
 
Symbols:
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_METACLASS_$_NSObject
+ __objc_empty_cache
+ _objc_alloc_init
+ _objc_enumerationMutation
+ _objc_msgSendSuper2
+ _objc_opt_new
+ _objc_release_x21
CStrings:
+ "%!X(MISSING)"
+ "%!@(MISSING)/"
+ "%!@(MISSING)/%!@(MISSING)"
+ "%!@(MISSING)/(appv|(|mansta-)fCfg|pcrt|scrt|seal)-%!@(MISSING)/ "
+ "%!@(MISSING)/(|mansta-)lcrt-%!@(MISSING)/ "
+ "%!@(MISSING)/trustobject-current/ /%!s(MISSING)/"
+ "%!s(MISSING) the contents of '%!@(MISSING)' (exceptionList: %!@(MISSING))"
+ "%!s(MISSING)/System/Library/Caches"
+ "%!s(MISSING)/System/Library/Caches/com.apple.kernelcaches"
+ "%!s(MISSING)/usr/standalone/firmware"
+ "%!s(MISSING)/usr/standalone/firmware/FUD"
+ "%!s(MISSING): %!s(MISSING)"
+ "%!s(MISSING): Could not create exceptions dictionary"
+ "%!s(MISSING): Failed to allocate %!d(MISSING) bytes for SHA calculation"
+ "%!s(MISSING): Failed to allocate %!d(MISSING) bytes for SHA result string"
+ "%!s(MISSING): Failed to open '%!s(MISSING)': %!s(MISSING)"
+ "%!s(MISSING): Failed to read from input file: %!s(MISSING)"
+ "%!s(MISSING): Found '/private/preboot/active' to point to '%!s(MISSING)'"
+ "%!s(MISSING): Running on an %!s(MISSING) build according to OS variant"
+ "%!s(MISSING): Verified 'trustobject-current' and '%!s(MISSING)' have the same content SHA-256 which also matches the name"
+ "%!s(MISSING): found %!s(MISSING) in bootargs(%!s(MISSING))"
+ "%!s(MISSING): safeObliterate: Cleaning Hardware volume"
+ "%!s(MISSING): safeObliterate: Cleaning Preboot volume"
+ "-[DiskSupport removeFSItem:error:]"
+ "-[DiskSupport traverseFolderAndRemoveItems:exceptions:]"
+ "/([^/]+)/ *"
+ "/([^/]+)/[ \t]*([^ \t/]*)"
+ "/FactoryData/System/Library/Caches/com.apple.factorydata/"
+ "/defaultAction/"
+ "0x"
+ "==> auto-traverse due to '%!@(MISSING)'"
+ "==> keepExcept for '%!@(MISSING)/%!@(MISSING)' has rule '%!@(MISSING)', using it instead of 'remove'"
+ "==> removeExcept for '%!@(MISSING)/%!@(MISSING)' has rule '%!@(MISSING)', using it instead of 'keep'"
+ "@16@0:8"
+ "According to rules, '%!@(MISSING)' will be %!s(MISSING)"
+ "B"
+ "B16@0:8"
+ "B32@0:8@16@24"
+ "B32@0:8@16^@24"
+ "Customer"
+ "DarwinInitCache"
+ "Deleting FS item '%!@(MISSING)'"
+ "DiskSupport"
+ "Error: Failed to delete '%!@(MISSING)' with error %!@(MISSING)!"
+ "Exception '%!@(MISSING)' for '%!@(MISSING)' is ill-formatted - found extra string '%!@(MISSING)' or missing '/'!"
+ "Exception '%!@(MISSING)' for '%!@(MISSING)' is ill-formatted!"
+ "FactoryData/System/Library/Caches"
+ "FactoryData/System/Library/Caches/com.apple.factorydata"
+ "Found exception '%!@(MISSING)' for '%!@(MISSING)'"
+ "Found regexp-exception '%!@(MISSING)' for '%!@(MISSING)', regexp '%!@(MISSING)'"
+ "Keeping"
+ "MobileActivation"
+ "Removing"
+ "TB,N,V_dryRunOnly"
+ "UniqueDeviceID"
+ "_dryRunOnly"
+ "active"
+ "arrayWithObjects:"
+ "arrayWithObjects:count:"
+ "bootArgsContains"
+ "calculate_SHA256_str"
+ "componentsSeparatedByString:"
+ "containsString:"
+ "contentsOfDirectoryAtPath:error:"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "defaultManager"
+ "dryRunOnly"
+ "epdm_fixup_hardware_volume"
+ "epdm_fixup_preboot"
+ "epdm_skip_hwvolume_cleanup=1"
+ "epdm_skip_preboot_cleanup=1"
+ "hasPrefix:"
+ "init"
+ "isEqualToString:"
+ "keep"
+ "keepExcept "
+ "keepExcept /"
+ "kept"
+ "kern.bootargs"
+ "length"
+ "matchesInString:options:range:"
+ "objectAtIndex:"
+ "objectAtIndexedSubscript:"
+ "objectForKeyedSubscript:"
+ "pathWithComponents:"
+ "r5pA2qLgR86BQKwgMjPWzg"
+ "rangeAtIndex:"
+ "rangeOfFirstMatchInString:options:range:"
+ "rangeOfString:"
+ "regularExpressionWithPattern:options:error:"
+ "remove"
+ "removeExcept "
+ "removeExcept %!@(MISSING)"
+ "removeExcept /"
+ "removeExcept /(ANE|GFX|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor))\\.img4/"
+ "removeExcept /apticket.der/"
+ "removeExcept /apticket.der/ /com.apple.factorydata/"
+ "removeExcept /devicetree.img4/ /root_hash.img4/ /sep-firmware.img4/"
+ "removeExcept /kernelcache/"
+ "removeFSItem:error:"
+ "removeItemAtPath:error:"
+ "removeObjectForKey:"
+ "removed"
+ "runningInternalBuild_block_invoke"
+ "setDryRunOnly:"
+ "setObject:forKey:"
+ "sharedInstance"
+ "stringByAppendingString:"
+ "stringWithFormat:"
+ "stringWithUTF8String:"
+ "subarrayWithRange:"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "substringWithRange:"
+ "traverse"
+ "traverseFolderAndRemoveItems:exceptions:"
+ "trustobject-%!s(MISSING)"
+ "trustobject-current"
+ "uppercaseString"
+ "v20@0:8B16"
- "ReleaseType"

```
