## com.apple.FTLivePhotoService

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService`

```diff

-1431.400.41.2.1
-  __TEXT.__text: 0x2b9ac
-  __TEXT.__auth_stubs: 0xfa0
+1431.500.151.2.9
+  __TEXT.__text: 0x2cf54
+  __TEXT.__auth_stubs: 0xfc0
   __TEXT.__objc_stubs: 0x15e0
   __TEXT.__objc_methlist: 0x9f4
-  __TEXT.__cstring: 0x29c9
+  __TEXT.__cstring: 0x2e09
   __TEXT.__objc_classname: 0x16c
-  __TEXT.__objc_methname: 0x2a2a
+  __TEXT.__objc_methname: 0x2a40
   __TEXT.__objc_methtype: 0x1420
   __TEXT.__oslogstring: 0x13dd
   __TEXT.__const: 0xc90

   __TEXT.__swift5_types: 0x7c
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_capture: 0x320
-  __TEXT.__unwind_info: 0xbfc
-  __TEXT.__eh_frame: 0x1068
-  __DATA_CONST.__auth_got: 0x7e0
+  __TEXT.__unwind_info: 0xbe4
+  __TEXT.__eh_frame: 0x1088
+  __DATA_CONST.__auth_got: 0x7f0
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__auth_ptr: 0x48
+  __DATA_CONST.__auth_ptr: 0x50
   __DATA_CONST.__const: 0x1a50
   __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x80
+  __DATA_CONST.__objc_classrefs: 0x188
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x2a08
   __DATA.__objc_selrefs: 0x840
-  __DATA.__objc_protorefs: 0x80
-  __DATA.__objc_classrefs: 0x188
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x58
   __DATA.__objc_data: 0x1258
-  __DATA.__data: 0x1078
+  __DATA.__data: 0x1058
   __DATA.__bss: 0xd40
   __DATA.__common: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1188
+  Functions: 1198
   Symbols:   278
-  CStrings:  921
+  CStrings:  938
 
CStrings:
+ "Already processing message with UUID %{public}s"
+ "AudioManager start failed with error %{public}@"
+ "Called %{public}s with state %{public}s"
+ "Cleaning up video message at URL %{public}s"
+ "Couldn't find processing request that apparently finished %{public}s"
+ "Discarding message %{public}s"
+ "Failed to clean up video message %{public}s"
+ "Failed to create video message folder %{public}@"
+ "Failed to move video message to accesible folder %{public}@"
+ "Failed to send video message using daemon %{public}@"
+ "Fatal error"
+ "Finished processing message %{public}s"
+ "Found message, moving video from %{public}s to %{public}s"
+ "Generating new request for AVCMomentsMediaType %{public}s"
+ "Insufficient space allocated to copy string contents"
+ "Invalid state '%{public}s' expected '%{public}s'"
+ "MessageController ended recording with UUID %{public}s"
+ "MessageController resetting for session %{public}s"
+ "MessageController saved video message with new asset identifier %{public}s"
+ "MessageController saving video message %{public}s"
+ "MessageController sending message with uuid %{public}s"
+ "MessageController started recording with UUID %{public}s"
+ "MessageController will end recording with UUID %{public}s"
+ "MessageController will start recording mediaType %{public}s"
+ "Moments capabilities changed %{public}s"
+ "Moments finished processing request %{public}s"
+ "Moments finished processing request %{public}s with error %{public}s"
+ "Moments finished request %{public}s"
+ "Moments finished request %{public}s with error %{public}s"
+ "Moments started processing request %{public}s"
+ "Moments started processing request %{public}s with error %{public}s"
+ "Rejecting current active request %{public}s"
+ "Started processing message with UUID %{public}s"
+ "State transform from '%{public}s' to '%{public}s' succeeded"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unable to find message %{public}s in processed store"
+ "Unable to find message %{public}s in processing store"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "invalid Collection: less than 'count' elements in collection"
- "Already processing message with UUID %s"
- "AudioManager start failed with error %@"
- "Called %s with state %s"
- "Cleaning up video message at URL %s"
- "Couldn't find processing request that apparently finished %s"
- "Discarding message %s"
- "Failed to clean up video message %s"
- "Failed to create view message folder %@"
- "Failed to move video message to accesible folder %@"
- "Failed to send video message using daemon %@)"
- "Finished processing message %s"
- "Found message, moving video from %s to %s"
- "Generating new request for AVCMomentsMediaType %s"
- "Invalid state '%s' expected '%s'"
- "MessageController ended recording with UUID %s"
- "MessageController resetting for session %s"
- "MessageController saved video message with new asset identifier %s"
- "MessageController saving video message %s"
- "MessageController sending message with uuid %s"
- "MessageController started recording with UUID %s"
- "MessageController will end recording with UUID %s"
- "MessageController will start recording mediaType %s"
- "Moments capabilities changed %s"
- "Moments finished processing request %s"
- "Moments finished processing request %s with error %s"
- "Moments finished request %s"
- "Moments finished request %s with error %s"
- "Moments started processing request %s"
- "Moments started processing request %s with error %s"
- "Rejecting current active request %s"
- "Started processing message with UUID %s"
- "State transform from '%s' to '%s' succeeded"
- "Unable to find message %s in processed store"
- "Unable to find message %s in processing store"

```
