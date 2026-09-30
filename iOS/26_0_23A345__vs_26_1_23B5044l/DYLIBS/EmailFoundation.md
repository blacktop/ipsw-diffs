## EmailFoundation

> `/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation`

```diff

-3864.100.1.2.9
-  __TEXT.__text: 0x66318
-  __TEXT.__auth_stubs: 0x14d0
+3864.200.33.2.2
+  __TEXT.__text: 0x65120
+  __TEXT.__auth_stubs: 0x1460
   __TEXT.__objc_methlist: 0x66b4
-  __TEXT.__gcc_except_tab: 0xc320
-  __TEXT.__const: 0x1fa
-  __TEXT.__cstring: 0x4897
-  __TEXT.__oslogstring: 0xfdf
+  __TEXT.__gcc_except_tab: 0xc068
+  __TEXT.__const: 0x1ea
+  __TEXT.__cstring: 0x47a7
+  __TEXT.__oslogstring: 0xdad
   __TEXT.__ustring: 0x144
   __TEXT.__swift5_typeref: 0xda
   __TEXT.__swift5_capture: 0xd0

   __TEXT.__swift5_fieldmd: 0x7c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x4b10
+  __TEXT.__unwind_info: 0x4ae0
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0xe72
-  __TEXT.__objc_methname: 0xc370
+  __TEXT.__objc_methname: 0xc2a0
   __TEXT.__objc_methtype: 0x1c0d
-  __TEXT.__objc_stubs: 0x8ba0
-  __DATA_CONST.__got: 0x778
-  __DATA_CONST.__const: 0x2120
+  __TEXT.__objc_stubs: 0x8ac0
+  __DATA_CONST.__got: 0x748
+  __DATA_CONST.__const: 0x20f8
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34f8
+  __DATA_CONST.__objc_selrefs: 0x34c0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x398
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0xa80
-  __AUTH_CONST.__const: 0x11c0
-  __AUTH_CONST.__cfstring: 0x56a0
+  __AUTH_CONST.__auth_got: 0xa48
+  __AUTH_CONST.__const: 0x1140
+  __AUTH_CONST.__cfstring: 0x5580
   __AUTH_CONST.__objc_const: 0xc348
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28

   __DATA.__objc_ivar: 0x524
   __DATA.__data: 0xf28
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x208
+  __DATA.__bss: 0x200
   __DATA_DIRTY.__objc_data: 0x22b0
   __DATA_DIRTY.__data: 0x1
-  __DATA_DIRTY.__bss: 0x32c
+  __DATA_DIRTY.__bss: 0x2e4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DE2D9650-0563-3550-8ECD-74EE4A43281D
-  Functions: 2663
-  Symbols:   10141
-  CStrings:  4354
+  UUID: 1AF8923E-30F8-3C28-9E1A-DF8FB278CF23
+  Functions: 2647
+  Symbols:   10070
+  CStrings:  4312
 
Symbols:
- _EFSaveTailspin.cold.1
- _EFSaveTailspin.cold.2
- _EFSaveTailspin.cold.3
- _EFSaveTailspin.cold.4
- _EFSaveTailspin.cold.5
- _EFSaveTailspin.cold.6
- _NSFileSize
- _TSPDumpOptions_CollectOsLogs
- _TSPDumpOptions_CollectOsSignposts
- _TSPDumpOptions_MinTimestamp
- _TSPDumpOptions_ReasonString
- _TSPDumpOptions_ScrubOutput
- ____generateTailspin_block_invoke
- ____generateTailspin_block_invoke.cold.1
- ____generateTailspin_block_invoke.cold.2
- ____generateTailspin_block_invoke.cold.3
- ____generateTailspin_block_invoke.cold.4
- ____shouldSaveTailspin_block_invoke
- ____systemTimeScale_block_invoke
- ____tailspinMinTimestamp_block_invoke
- ____tailspinMinTimestamp_block_invoke.cold.1
- ____temporaryTailspinPath_block_invoke
- ___block_descriptor_44_ea8_32s_e8_v12?0B8ls32l8
- ___block_literal_global.101
- ___block_literal_global.115
- ___block_literal_global.86
- __os_assumes_log
- __os_feature_enabled_impl
- __shouldSaveTailspin.last
- __shouldSaveTailspin.lock
- __shouldSaveTailspin.o
- __shouldSaveTailspin.threshold
- __systemTimeScale.machTimebaseInfo
- __systemTimeScale.o
- __tailspinMinTimestamp.absoluteTicksBeforeNow
- __tailspinMinTimestamp.o
- __temporaryTailspinPath.filenameFormatter
- __temporaryTailspinPath.o
- _fsync
- _mach_absolute_time
- _mach_continuous_time
- _mach_timebase_info
- _objc_msgSend$attributesOfItemAtPath:error:
- _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
- _objc_msgSend$fileExistsAtPath:isDirectory:
- _objc_msgSend$integerForKey:
- _objc_msgSend$localizedDescription
- _objc_msgSend$moveItemAtPath:toPath:error:
- _objc_msgSend$setDateFormat:
- _tailspin_dump_output_with_options
CStrings:
- "%@/%@"
- "%@/mailspin-%@-%@.tailspin"
- "%s"
- "%s: "
- "/var/mobile/Library/Caches/com.apple.backboardd/spool"
- "/var/mobile/Library/Mail/tailspin-work"
- "Attempting mailspin for: %{public}s"
- "Could not reach spool directory?!"
- "Could not reach working directory?!"
- "DiagnosticPipeline"
- "Empty tailspin file: %{public}@"
- "Failed move %{public}@ -> %{public}@: %{public}s"
- "Failed to open %{public}@: %{darwin.errno}d"
- "Mail"
- "Mail EFTailspin: "
- "Mailspin failure!"
- "Mailspin success: %{public}s"
- "MinimumSecondsBetweenTailspins"
- "Non-standard tailspin rate limit: %ld minimum seconds between tailspins"
- "Saving tailspin for %{public}s"
- "Skipping tailspin for %{public}s"
- "Standard tailspin rate limit: %d minimum seconds between tailspins"
- "Successful move %{public}@ -> %{public}@"
- "Unable to create %{public}@: %{public}s"
- "attributesOfItemAtPath:error:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "fileExistsAtPath:isDirectory:"
- "integerForKey:"
- "localizedDescription"
- "moveItemAtPath:toPath:error:"
- "setDateFormat:"
- "v12@?0B8"
- "yyyy-MMdd-HHmm-ssSSS"

```
