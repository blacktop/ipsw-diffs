## RCS

> `/System/Library/Messages/PlugIns/RCS.imservice/Contents/MacOS/RCS`

```diff

-1402.400.131.1.3
-  __TEXT.__text: 0x6f3b8
-  __TEXT.__auth_stubs: 0x1570
+1402.500.181.1.1
+  __TEXT.__text: 0x738c4
+  __TEXT.__auth_stubs: 0x1540
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__objc_methlist: 0x23c
-  __TEXT.__const: 0x2560
+  __TEXT.__objc_methlist: 0x544
+  __TEXT.__const: 0x2590
   __TEXT.__objc_classname: 0x7c
-  __TEXT.__objc_methname: 0x21ab
+  __TEXT.__objc_methname: 0x22f3
   __TEXT.__objc_methtype: 0xc5c
-  __TEXT.__cstring: 0x16b5
-  __TEXT.__constg_swiftt: 0xfd8
-  __TEXT.__swift5_typeref: 0xf15
-  __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0x830
+  __TEXT.__cstring: 0x1375
+  __TEXT.__constg_swiftt: 0x1050
+  __TEXT.__swift5_typeref: 0xf81
+  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_reflstr: 0x873
   __TEXT.__swift5_assocty: 0x168
-  __TEXT.__oslogstring: 0x19ea
+  __TEXT.__oslogstring: 0x1d86
+  __TEXT.__swift5_fieldmd: 0xd9c
   __TEXT.__swift5_proto: 0x1f0
-  __TEXT.__swift5_types: 0xf8
-  __TEXT.__swift5_fieldmd: 0xd44
+  __TEXT.__swift5_types: 0xfc
+  __TEXT.__swift_as_entry: 0xe8
+  __TEXT.__swift_as_ret: 0x100
   __TEXT.__swift5_capture: 0x310
   __TEXT.__swift5_mpenum: 0x68
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__unwind_info: 0x19d0
-  __TEXT.__eh_frame: 0x31e4
-  __DATA_CONST.__auth_got: 0xac0
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__auth_ptr: 0x300
-  __DATA_CONST.__const: 0x2ac0
+  __TEXT.__unwind_info: 0x1930
+  __TEXT.__eh_frame: 0x34d4
+  __DATA_CONST.__auth_got: 0xaa8
+  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__auth_ptr: 0x330
+  __DATA_CONST.__const: 0x2c20
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA.__objc_const: 0x1760
-  __DATA.__objc_selrefs: 0x740
-  __DATA.__objc_data: 0x348
-  __DATA.__data: 0x1f18
+  __DATA.__objc_const: 0x11e8
+  __DATA.__objc_selrefs: 0x990
+  __DATA.__objc_data: 0x370
+  __DATA.__data: 0x1f58
   __DATA.__bss: 0x3a80
   __DATA.__common: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/CoreTelephony.framework/Versions/A/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CommunicationsFilter.framework/Versions/A/CommunicationsFilter
+  - /System/Library/PrivateFrameworks/IDSFoundation.framework/Versions/A/IDSFoundation
   - /System/Library/PrivateFrameworks/IMDaemonCore.framework/Versions/A/IMDaemonCore
   - /System/Library/PrivateFrameworks/IMFoundation.framework/Versions/A/IMFoundation
   - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/Versions/A/IMSharedUtilities

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E474E356-8878-3B6D-9F41-99AC813A87A1
-  Functions: 1923
-  Symbols:   241
-  CStrings:  632
+  UUID: 8B5783DF-213A-3F27-AFDE-C59D623A2407
+  Functions: 1899
+  Symbols:   248
+  CStrings:  650
 
Symbols:
+ _IDSRegistrationPropertySupportsRBMChatBot
+ _IMPersistentMenuAttributeName
+ _OBJC_CLASS_$_IMBrandInfo
+ _OBJC_CLASS_$_IMMultiplexingServiceReachabilityResponseHandler
+ _OBJC_CLASS_$_IMPersistentMenu
+ _OBJC_CLASS_$_IMServiceReachabilityResponseBlockHandler
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ _swift_setDeallocating
- __swift_FORCE_LOAD_$_swiftFileProvider
CStrings:
+ "%s reachable because is bot and supports chat"
+ "%s reachable because supports text and transfer"
+ "%s unreachable beacuse doesn't support chat"
+ "%s unreachable because destination is offline and this is not a group"
+ "Discarding newValue %s for rawURI, invalid version %ld"
+ "Invalid group URI %s, expected scheme `sip`, actual is %s"
+ "Invalid version %ld, groupID %s is not valid"
+ "Missing rawURI for groupID %s"
+ "RCSHandle %s does not respresent a group URI, but is called in a group identity context."
+ "URI is likely a Jio URI -- bypassing group URI check"
+ "Unable to create RCSHandle for uri %s: %s"
+ "Unable to create RCSHandle from rawURI %s with error %s"
+ "Unknown identity version %ld, unable to generate raw group focus URI."
+ "Update brand info %s for chat %s, brand logo guid: %s, brand logo data: %ld"
+ "Update empty stamp menu for chat %s"
+ "Update persistent menu %s for chat %s"
+ "__im_isChatBotPatterned"
+ "allExistingChatsWithIdentifier:"
+ "brandInfoDictionary"
+ "brandLogoData"
+ "brandLogoGuid"
+ "chatStyle"
+ "com.apple.Messages"
+ "creating a new chatIdentifer %sfor incoming group %s, participants count except self: %ld"
+ "displayText"
+ "emptyStampProperty"
+ "handleID"
+ "initWithBlock:"
+ "initWithResponseHandlers:"
+ "isChatBot"
+ "isEmptyStamped:"
+ "isRelayChatBotEnabled"
+ "name"
+ "ob"
+ "persistentMenuDictionary"
+ "rcs.advised-action"
+ "requestBrandInfo"
+ "requestPersistentMenu"
+ "setRcsAdvisedAction:"
+ "transport"
+ "updateBrandLogo:transferGuid:"
+ "updateProperties:shouldBroadcast:"
+ "v24@?0@\"IMServiceReachabilityRequest\"8@\"IMServiceReachabilityResult\"16"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Skipping path component %s in RCS URI %s: not a valid pair"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "X-Apple-ExampleHeader"
- "creating a new chatIdentifer %sfor incoming group %s"
- "finalResultForService:handleIDs:allAreReachable:checkedServer:error:"
- "invalid Collection: less than 'count' elements in collection"

```
