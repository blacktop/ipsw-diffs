## AppleHIDFeedback

> `/System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback`

```diff

-5.1.0.0.0
-  __TEXT.__text: 0x19ac
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x13c
+12.0.0.0.0
+  __TEXT.__text: 0x4da8
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_methlist: 0x324
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x392
-  __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__oslogstring: 0x130
-  __TEXT.__unwind_info: 0xe4
-  __TEXT.__objc_classname: 0x27
-  __TEXT.__objc_methname: 0x4f6
-  __TEXT.__objc_methtype: 0x102
-  __TEXT.__objc_stubs: 0x440
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__cstring: 0x81e
+  __TEXT.__oslogstring: 0x685
+  __TEXT.__gcc_except_tab: 0x190
+  __TEXT.__unwind_info: 0x18c
+  __TEXT.__objc_classname: 0x58
+  __TEXT.__objc_methname: 0xc46
+  __TEXT.__objc_methtype: 0x1b3
+  __TEXT.__objc_stubs: 0x9e0
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__const: 0x130
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x158
-  __DATA_CONST.__objc_selrefs: 0x178
-  __DATA_CONST.__objc_classrefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0x40
+  __DATA_CONST.__objc_const: 0x418
+  __DATA_CONST.__objc_selrefs: 0x350
+  __DATA_CONST.__objc_classrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_arraydata: 0x100
+  __AUTH_CONST.__cfstring: 0x5a0
+  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_const: 0x168
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0xd8
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1c8
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x14
+  __AUTH_CONST.__objc_dictobj: 0xa0
+  __AUTH_CONST.__auth_got: 0x230
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x40
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 38
-  Symbols:   231
-  CStrings:  114
+  Functions: 89
+  Symbols:   441
+  CStrings:  280
 
Symbols:
+ -[AHFManager pencilController]
+ -[AHFManager setPencilController:]
+ -[AHFPencilController .cxx_destruct]
+ -[AHFPencilController availableDigitizerStylus]
+ -[AHFPencilController availableOpaqueTouch]
+ -[AHFPencilController availablePencilHaptics]
+ -[AHFPencilController dealloc]
+ -[AHFPencilController digitizerStylusClient]
+ -[AHFPencilController init]
+ -[AHFPencilController initializeDigitizerStylusSystem]
+ -[AHFPencilController initializeOpaqueTouchSystem]
+ -[AHFPencilController initializePencilHapticsSystem]
+ -[AHFPencilController opaqueTouchClient]
+ -[AHFPencilController patternsLibrary]
+ -[AHFPencilController pencilHapticsClient]
+ -[AHFPencilController playFeedback:accessoryID:timestamp:error:]
+ -[AHFPencilController playFeedback:senderID:timestamp:error:]
+ -[AHFPencilController playFeedbackGated:haptics:timestamp:error:]
+ -[AHFPencilController prevTimestampUs]
+ -[AHFPencilController queue]
+ -[AHFPencilController setAvailableDigitizerStylus:]
+ -[AHFPencilController setAvailableOpaqueTouch:]
+ -[AHFPencilController setAvailablePencilHaptics:]
+ -[AHFPencilController setDigitizerStylusClient:]
+ -[AHFPencilController setOpaqueTouchClient:]
+ -[AHFPencilController setPatternsLibrary:]
+ -[AHFPencilController setPencilHapticsClient:]
+ -[AHFPencilController setPrevTimestampUs:]
+ -[AHFPencilController setQueue:]
+ -[AHFPencilPatternLibrary .cxx_destruct]
+ -[AHFPencilPatternLibrary allPatterns]
+ -[AHFPencilPatternLibrary createPatternsLibraryFrom:]
+ -[AHFPencilPatternLibrary getReportForPattern:timestampUs:prevTimestampUs:error:]
+ -[AHFPencilPatternLibrary init]
+ -[AHFPencilPatternLibrary init].cold.1
+ -[AHFPencilPatternLibrary isReport:equalTo:]
+ -[AHFPencilPatternLibrary library]
+ -[AHFPencilPatternLibrary maybeGetExploratoryPayload:]
+ -[AHFPencilPatternLibrary setLibrary:]
+ -[AHFPencilPatternLibrary waveformIndexWithType:]
+ GCC_except_table12
+ GCC_except_table16
+ GCC_except_table5
+ GCC_except_table6
+ GCC_except_table8
+ GCC_except_table9
+ _IOObjectRelease
+ _IORegistryEntryIDMatching
+ _IORegistryEntrySearchCFProperty
+ _IORegistryEntrySetCFProperty
+ _IOServiceGetMatchingService
+ _OBJC_CLASS_$_AHFPencilController
+ _OBJC_CLASS_$_AHFPencilPatternLibrary
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSURL
+ _OBJC_IVAR_$_AHFManager._pencilController
+ _OBJC_IVAR_$_AHFPencilController._availableDigitizerStylus
+ _OBJC_IVAR_$_AHFPencilController._availableOpaqueTouch
+ _OBJC_IVAR_$_AHFPencilController._availablePencilHaptics
+ _OBJC_IVAR_$_AHFPencilController._digitizerStylusClient
+ _OBJC_IVAR_$_AHFPencilController._opaqueTouchClient
+ _OBJC_IVAR_$_AHFPencilController._patternsLibrary
+ _OBJC_IVAR_$_AHFPencilController._pencilHapticsClient
+ _OBJC_IVAR_$_AHFPencilController._prevTimestampUs
+ _OBJC_IVAR_$_AHFPencilController._queue
+ _OBJC_IVAR_$_AHFPencilPatternLibrary._library
+ _OBJC_METACLASS_$_AHFPencilController
+ _OBJC_METACLASS_$_AHFPencilPatternLibrary
+ __OBJC_$_INSTANCE_METHODS_AHFPencilController
+ __OBJC_$_INSTANCE_METHODS_AHFPencilPatternLibrary
+ __OBJC_$_INSTANCE_VARIABLES_AHFPencilController
+ __OBJC_$_INSTANCE_VARIABLES_AHFPencilPatternLibrary
+ __OBJC_$_PROP_LIST_AHFPencilController
+ __OBJC_$_PROP_LIST_AHFPencilPatternLibrary
+ __OBJC_CLASS_RO_$_AHFPencilController
+ __OBJC_CLASS_RO_$_AHFPencilPatternLibrary
+ __OBJC_METACLASS_RO_$_AHFPencilController
+ __OBJC_METACLASS_RO_$_AHFPencilPatternLibrary
+ ___31-[AHFPencilPatternLibrary init]_block_invoke
+ ___50-[AHFPencilController initializeOpaqueTouchSystem]_block_invoke
+ ___50-[AHFPencilController initializeOpaqueTouchSystem]_block_invoke.24
+ ___52-[AHFPencilController initializePencilHapticsSystem]_block_invoke
+ ___52-[AHFPencilController initializePencilHapticsSystem]_block_invoke.35
+ ___54-[AHFPencilController initializeDigitizerStylusSystem]_block_invoke
+ ___54-[AHFPencilController initializeDigitizerStylusSystem]_block_invoke.13
+ ___61-[AHFPencilController playFeedback:senderID:timestamp:error:]_block_invoke
+ ___64-[AHFPencilController playFeedback:accessoryID:timestamp:error:]_block_invoke
+ ___block_descriptor_40_e8_32s_e15_B32?0816^B24ls32l8
+ ___block_descriptor_80_e8_32s40s48r56r64w_e5_v8?0lw64l8r48l8r56l8s32l8s40l8
+ __os_log_debug_impl
+ __os_log_error_impl
+ __os_signpost_emit_with_name_impl
+ __unnamed_array_storage.12
+ __unnamed_array_storage.21
+ __unnamed_array_storage.22
+ __unnamed_array_storage.32
+ __unnamed_array_storage.33
+ __unnamed_array_storage.68
+ _kCFAllocatorDefault
+ _kIOMainPortDefault
+ _mach_error_string
+ _objc_autoreleaseReturnValue
+ _objc_msgSend$URLsForResourcesWithExtension:subdirectory:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addIndex:
+ _objc_msgSend$allKeys
+ _objc_msgSend$availableDigitizerStylus
+ _objc_msgSend$availableOpaqueTouch
+ _objc_msgSend$availablePencilHaptics
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$bytes
+ _objc_msgSend$containsIndex:
+ _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
+ _objc_msgSend$count
+ _objc_msgSend$createPatternsLibraryFrom:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionaryWithContentsOfURL:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$getReportForPattern:timestampUs:prevTimestampUs:error:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$initializeDigitizerStylusSystem
+ _objc_msgSend$initializeOpaqueTouchSystem
+ _objc_msgSend$initializePencilHapticsSystem
+ _objc_msgSend$integerValue
+ _objc_msgSend$isEqualToData:
+ _objc_msgSend$keysOfEntriesPassingTest:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$length
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$maybeGetExploratoryPayload:
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$pencilController
+ _objc_msgSend$playFeedbackGated:haptics:timestamp:error:
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$removeIndex:
+ _objc_msgSend$setAvailablePencilHaptics:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$waveformIndexWithType:
+ _objc_opt_class
+ _objc_retain
+ _os_signpost_enabled
- __unnamed_array_storage.35
CStrings:
+ "\x02"
+ "\x12\x15"
+ "%s Correctly added pattern '%@' (%@) to library (priority=%@, timeout=%@): %@"
+ "%s Could load %@"
+ "%s Could not find a 'Gain' in asset %u in %@"
+ "%s Could not find a 'Num Loops' in %@ or number of loops invalid (0)"
+ "%s Could not find a 'Pattern' in %@"
+ "%s Could not find a 'Priority' in %@"
+ "%s Could not find a 'Spacing' in asset %u in %@"
+ "%s Could not find a 'Timeout' in %@"
+ "%s Could not find a 'Type' in asset %u in %@"
+ "%s Could not find a name for pattern in %@"
+ "%s Could not understand 'Type' in asset %u in %@"
+ "%s Digitizer Stylus with senderID 0x%llx added in %s queue"
+ "%s Digitizer Stylus with senderID 0x%llx removed in %s queue"
+ "%s Invalid value for 'Gain' in asset %u in %@"
+ "%s Loaded %lu haptics patterns: %@"
+ "%s Loaded %lu internal haptics patterns: %@"
+ "%s OpaqueTouch with senderID 0x%llx added in %s queue"
+ "%s OpaqueTouch with senderID 0x%llx removed in %s queue"
+ "%s Pattern '%@' already exists in library. Overriding"
+ "%s Pattern '%@' is a exploratory '%@' with gain %u"
+ "%s Pencil Haptics with senderID 0x%llx added in %s queue"
+ "%s Pencil Haptics with senderID 0x%llx removed in %s queue"
+ "%s The following haptics patterns are being overriden: %@"
+ "%s Trying to play pattern %@ on pencil HID sender ID 0x%llX"
+ "%s Trying to play pattern %@ on pencil power source accessory ID %@"
+ "%s \\Array 'Pattern' is empty in %@"
+ "%{public, signpost.description:begin_time}llu"
+ "-[AHFPencilController initializeDigitizerStylusSystem]_block_invoke"
+ "-[AHFPencilController initializeOpaqueTouchSystem]_block_invoke"
+ "-[AHFPencilController initializePencilHapticsSystem]_block_invoke"
+ "-[AHFPencilController playFeedback:accessoryID:timestamp:error:]"
+ "-[AHFPencilController playFeedback:senderID:timestamp:error:]"
+ "-[AHFPencilController playFeedbackGated:haptics:timestamp:error:]"
+ "-[AHFPencilPatternLibrary createPatternsLibraryFrom:]"
+ "-[AHFPencilPatternLibrary init]"
+ "-[AHFPencilPatternLibrary maybeGetExploratoryPayload:]"
+ "/AppleInternal/Library/Application Support/AppleHIDFeedback/Patterns/Pencil"
+ "@\"AHFPencilController\""
+ "@\"AHFPencilPatternLibrary\""
+ "@\"NSDictionary\""
+ "@\"NSMutableIndexSet\""
+ "@24@0:8@16"
+ "@48@0:8@16Q24Q32o^@40"
+ "AHFPencilController"
+ "AHFPencilPatternLibrary"
+ "AppleEmbeddedBluetoothHaptics"
+ "B32@0:8@16@24"
+ "B32@?0@8@16^B24"
+ "Error requesting playback to kernel: %s"
+ "Gain"
+ "HapticsMessage"
+ "I"
+ "I16@0:8"
+ "IOClass"
+ "IOService"
+ "MicroTap"
+ "MiniTap"
+ "No Pencil Haptics device to play pattern %@ to"
+ "Num Loops"
+ "Pattern"
+ "Patterns/Pencil"
+ "Pencil"
+ "PhysicalDeviceUniqueID"
+ "PlayPencilFeedback"
+ "Priority"
+ "Spacing"
+ "T@\"AHFPencilController\",&,N,V_pencilController"
+ "T@\"AHFPencilPatternLibrary\",&,N,V_patternsLibrary"
+ "T@\"HIDEventSystemClient\",&,N,V_digitizerStylusClient"
+ "T@\"HIDEventSystemClient\",&,N,V_opaqueTouchClient"
+ "T@\"HIDEventSystemClient\",&,N,V_pencilHapticsClient"
+ "T@\"NSDictionary\",&,N,V_library"
+ "T@\"NSMutableIndexSet\",&,N,V_availableDigitizerStylus"
+ "T@\"NSMutableIndexSet\",&,N,V_availableOpaqueTouch"
+ "TI,N,V_availablePencilHaptics"
+ "Timeout"
+ "Too soon after previous haptic (delta %lluus)"
+ "Type"
+ "URLsForResourcesWithExtension:subdirectory:"
+ "WideTap"
+ "_availableDigitizerStylus"
+ "_availableOpaqueTouch"
+ "_availablePencilHaptics"
+ "_digitizerStylusClient"
+ "_library"
+ "_opaqueTouchClient"
+ "_patternsLibrary"
+ "_pencilController"
+ "_pencilHapticsClient"
+ "addEntriesFromDictionary:"
+ "addIndex:"
+ "allKeys"
+ "app_switcher"
+ "availableDigitizerStylus"
+ "availableOpaqueTouch"
+ "availablePencilHaptics"
+ "bundleForClass:"
+ "bytes"
+ "com.apple.hid.AppleHIDFeedback.Pencil"
+ "containsIndex:"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "context_menu"
+ "count"
+ "createPatternsLibraryFrom:"
+ "dataWithBytes:length:"
+ "defaultManager"
+ "dictionaryWithContentsOfURL:"
+ "digitizerStylusClient"
+ "drag_drop_table_edit"
+ "edge"
+ "empty_app_switcher"
+ "fileURLWithPath:"
+ "filteredArrayUsingPredicate:"
+ "generic_selection"
+ "getReportForPattern:timestampUs:prevTimestampUs:error:"
+ "hasPrefix:"
+ "i44@0:8@16I24Q28o^@36"
+ "index_bar_selection"
+ "initializeDigitizerStylusSystem"
+ "initializeOpaqueTouchSystem"
+ "initializePencilHapticsSystem"
+ "integerValue"
+ "isEqualToData:"
+ "isReport:equalTo:"
+ "keysOfEntriesPassingTest:"
+ "lastPathComponent"
+ "length"
+ "library"
+ "lowercaseString"
+ "maybeGetExploratoryPayload:"
+ "mutableBytes"
+ "mutableCopy"
+ "objectForKey:"
+ "opaqueTouchClient"
+ "page_control_selection"
+ "pathExtension == %@"
+ "pattern"
+ "patternsLibrary"
+ "pencilController"
+ "pencilHapticsClient"
+ "playFeedbackGated:haptics:timestamp:error:"
+ "predicateWithFormat:"
+ "refresh"
+ "removeIndex:"
+ "setAvailableDigitizerStylus:"
+ "setAvailableOpaqueTouch:"
+ "setAvailablePencilHaptics:"
+ "setDigitizerStylusClient:"
+ "setLibrary:"
+ "setOpaqueTouchClient:"
+ "setPatternsLibrary:"
+ "setPencilController:"
+ "setPencilHapticsClient:"
+ "setValue:forKey:"
+ "state"
+ "stringByDeletingPathExtension"
+ "stringWithFormat:"
+ "substringFromIndex:"
+ "swipe"
+ "unsignedIntValue"
+ "v20@0:8I16"
+ "valueForKey:"
+ "waveformIndexWithType:"

```
