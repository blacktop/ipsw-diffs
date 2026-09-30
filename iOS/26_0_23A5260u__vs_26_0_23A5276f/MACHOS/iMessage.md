## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1436.100.6.2.12
-  __TEXT.__text: 0xb41dc
-  __TEXT.__auth_stubs: 0x1a20
-  __TEXT.__objc_stubs: 0xbbc0
-  __TEXT.__objc_methlist: 0x2904
-  __TEXT.__const: 0xb88
+1440.100.7.2.5
+  __TEXT.__text: 0xb5f48
+  __TEXT.__auth_stubs: 0x1a70
+  __TEXT.__objc_stubs: 0xbc00
+  __TEXT.__objc_methlist: 0x2924
+  __TEXT.__const: 0xb98
   __TEXT.__gcc_except_tab: 0xb3a0
-  __TEXT.__cstring: 0x335d
-  __TEXT.__oslogstring: 0x15b76
-  __TEXT.__objc_classname: 0x509
-  __TEXT.__objc_methname: 0x11880
-  __TEXT.__objc_methtype: 0x28dc
+  __TEXT.__cstring: 0x339d
+  __TEXT.__oslogstring: 0x15ff6
+  __TEXT.__objc_classname: 0x50a
+  __TEXT.__objc_methname: 0x119fd
+  __TEXT.__objc_methtype: 0x290b
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x636
+  __TEXT.__swift5_typeref: 0x63e
   __TEXT.__constg_swiftt: 0x36c
   __TEXT.__swift5_reflstr: 0x2b0
   __TEXT.__swift5_fieldmd: 0x35c

   __TEXT.__swift5_types: 0x38
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__swift5_capture: 0x234
+  __TEXT.__swift5_capture: 0x264
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2270
+  __TEXT.__unwind_info: 0x2278
   __TEXT.__eh_frame: 0x630
-  __DATA_CONST.__auth_got: 0xd20
+  __DATA_CONST.__auth_got: 0xd48
   __DATA_CONST.__got: 0xfb8
-  __DATA_CONST.__auth_ptr: 0x160
-  __DATA_CONST.__const: 0x36c0
+  __DATA_CONST.__auth_ptr: 0x168
+  __DATA_CONST.__const: 0x3740
   __DATA_CONST.__cfstring: 0x3720
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x2df0
-  __DATA.__objc_selrefs: 0x37a8
-  __DATA.__objc_ivar: 0x1cc
+  __DATA.__objc_const: 0x2e20
+  __DATA.__objc_selrefs: 0x37c0
+  __DATA.__objc_ivar: 0x1d0
   __DATA.__objc_data: 0x9b8
   __DATA.__data: 0xa38
   __DATA.__bss: 0x7b0

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E095D016-2B34-304F-BD58-FEBFB07D5C2B
-  Functions: 1570
-  Symbols:   847
-  CStrings:  4905
+  UUID: AEAEE6F3-CE52-3687-A54B-86080642013C
+  Functions: 1582
+  Symbols:   845
+  CStrings:  4928
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftModelIO
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "About to send background request to %s."
+ "About to send dictionary to peer devices: %s toURIS: %@, from: %s"
+ "About to send dictionary: %s toURIS: %s, from: %s"
+ "Could not find chat for identifier: %s"
+ "Could not get background refresh info for chat properties %s"
+ "Did not broadcast asset change status item. Update type: %s."
+ "Failed to download background with transferID: %s. Error: %@, MMCS error info: %s. Success: %{bool}d, outTransferID: %s, path: %s"
+ "Failed to get necessary transfer info from background upload. Aborting send. Success: %{bool}d. TransferID: %s Owner ID: %s. Signature: %s. Request URL: %s. Encryption key: %s"
+ "Generated and broadcasted asset change status item. Update type: %s."
+ "Missing a necessary parameter in incoming background command: %s"
+ "Not downloading background for chat %@, already attempting a download for transfer ID: %s"
+ "Poster is sensitive: %{bool}d."
+ "Removing old poster path: %s"
+ "Successfully blastdoor'd data for background with transferID: %s. Error: %@"
+ "T@\"NSMutableSet\",R,N,V_transcriptBackgroundTransfersCurrentlyDownloading"
+ "Unable to respond to a background request because we don't have all the required properties. Current properties: %s"
+ "Writing poster to %s"
+ "_transcriptBackgroundTransfersCurrentlyDownloading"
+ "originalServiceName"
+ "retryBackgroundUpload"
+ "sendMessageDictionary:encryptDictionary:fromID:fromAccount:toURIs:toGroup:priority:options:willSendBlock:callCompletionOnSuccess:callCompletionOnLast:completionBlock:"
+ "setNewBackground"
+ "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:handle:error:"
+ "transcriptBackgroundTransfersCurrentlyDownloading"
+ "v100@0:8@16B24@28@36@44@52q60@68@?76B84B88@?92"
+ "v16@?0I8B12"
+ "v44@?0@\"MessageDeliveryController\"8@\"NSArray\"16B24I28B32B36B40"
- "Failed to download background with transferID: %s. Error: %@, MMCS error info: %s"
- "trackSentMessageEventOfType:subtype:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:handle:error:"
- "v12@?0I8"
- "v40@?0@\"MessageDeliveryController\"8@\"NSArray\"16B24I28B32B36"

```
