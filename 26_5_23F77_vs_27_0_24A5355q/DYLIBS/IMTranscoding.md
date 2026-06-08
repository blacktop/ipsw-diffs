## IMTranscoding

> `/System/Library/PrivateFrameworks/IMTranscoding.framework/IMTranscoding`

```diff

-1450.600.61.2.7
-  __TEXT.__text: 0x7b70
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x194
+1481.100.29.2.9
+  __TEXT.__text: 0x7a5c
+  __TEXT.__objc_methlist: 0x2c4
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x99c
-  __TEXT.__cstring: 0x50e
-  __TEXT.__oslogstring: 0x1172
-  __TEXT.__unwind_info: 0x228
-  __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methname: 0xc38
-  __TEXT.__objc_methtype: 0x371
-  __TEXT.__objc_stubs: 0x620
-  __DATA_CONST.__got: 0xb8
+  __TEXT.__gcc_except_tab: 0x760
+  __TEXT.__cstring: 0x522
+  __TEXT.__oslogstring: 0x1231
+  __TEXT.__unwind_info: 0x238
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x368
   __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x228
+  __DATA_CONST.__objc_selrefs: 0x300
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2c8
+  __DATA_CONST.__got: 0xd0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x240
-  __AUTH_CONST.__objc_const: 0x100
+  __AUTH_CONST.__objc_const: 0x268
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x8
+  __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Marco.framework/Marco
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6C687567-7CDF-3961-8E28-85ADA5DB421D
-  Functions: 60
-  Symbols:   125
-  CStrings:  259
+  UUID: 8134DEEA-4E3B-3E87-8309-0B00ECA05F52
+  Functions: 70
+  Symbols:   137
+  CStrings:  164
 
Symbols:
+ _IMPreviewGenerationErrorDomain
+ _IMUTITypeForExtension
+ _IMUTITypeIsAnimatedImage
+ _IMUTITypeIsPhoto
+ _IMUTITypeIsVideo
+ _OBJC_CLASS_$_IMFeatureFlags
+ _OBJC_CLASS_$_IMPreviewGenerationUtilities
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x10
+ _objc_retain_x2
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x9
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "IMGradientValues"
+ "received gradient image generation error for sourceURL: %@, %s"
+ "received reply for image gradient generation for sourceURL %@, error %@"
+ "received unknown error for image gradient generation %s"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@16@0:8"
- "B16@0:8"
- "IMTranscodeController"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_connectionQueue"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_connection"
- "URLByAppendingPathExtension:"
- "URLByDeletingLastPathComponent"
- "URLByDeletingPathExtension"
- "URLWithString:"
- "UTF8String"
- "__imArrayByApplyingBlock:"
- "_connect"
- "_connection"
- "_connectionQueue"
- "_decodeiMessageAppPayload:senderContext:bundleID:retries:completionBlock:blockUntilReply:"
- "_disconnected"
- "_generateMetadata:metadataURL:senderContext:constraints:retries:completionBlock:blockUntilReply:"
- "_generatePreview:previewURL:senderContext:constraints:retries:balloonBundleID:transferGUID:completionBlock:blockUntilReply:"
- "_generateSafeRender:constraints:retries:completionBlock:"
- "_insertSandboxExtensionIntoXPCMessage:withKey:forFileURL:readOnly:"
- "_randomTemporaryPathWithFileName:"
- "_transcodeFileTransferContents:utiType:isSticker:allowUnfilteredUTIs:target:sizes:commonCapabilities:maxDimension:transcoderUserInfo:representations:fallBack:retries:isLQMEnabled:completionBlock:"
- "_transcodeFileTransferPayloadData:balloonBundleID:attachments:retries:fallBack:completionBlock:"
- "absoluteString"
- "connection"
- "connectionQueue"
- "copyItemAtPath:toPath:error:"
- "copyItemAtURL:toURL:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "decodeiMessageAppPayload:senderContext:bundleID:completionBlock:blockUntilReply:"
- "defaultCenter"
- "defaultManager"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "fileURLWithPath:"
- "forceAutoBugCaptureWithSubType:errorPayload:"
- "generateMetadata:metadataURL:senderContext:constraints:completionBlock:"
- "generateMetadata:metadataURL:senderContext:constraints:completionBlock:blockUntilReply:"
- "generatePosterConfigFromSource:destination:senderContext:completionBlock:blockUntilReply:"
- "generatePreview:previewURL:senderContext:constraints:balloonBundleID:transferGUID:completionBlock:blockUntilReply:"
- "generateReadOnlyPosterConfig:completionBlock:"
- "generateSafeRender:completionBlock:"
- "generateSafeRender:constraints:completionBlock:"
- "generateSnapshotForMessageGUID:payloadURL:balloonBundleID:senderContext:completionBlock:"
- "getValue:size:"
- "im_randomTemporaryFileURLWithFileName:"
- "init"
- "isEqual:"
- "isInternalInstall"
- "isMainThread"
- "lastPathComponent"
- "length"
- "longLongValue"
- "maxTimeForTranscriptionInSeconds"
- "moveItemAtURL:toURL:error:"
- "objectForKey:"
- "path"
- "pathExtension"
- "postNotificationName:object:userInfo:"
- "q16@0:8"
- "removeItemAtURL:error:"
- "replaceTransferWithSafeTransfer:constraints:completionBlock:"
- "setConnection:"
- "setConnectionQueue:"
- "sharedInstance"
- "sharedInstanceForBagType:"
- "stringByAppendingPathExtension:"
- "stringByDeletingPathExtension"
- "stringWithFormat:"
- "transcodeFallbackFileTransferContents:utiType:allowUnfilteredUTIs:target:sizes:commonCapabilities:maxDimension:transcoderUserInfo:representations:isLQMEnabled:completionBlock:"
- "transcodeFallbackFileTransferPayloadData:balloonBundleID:attachments:completionBlock:"
- "transcodeFileTransferContents:utiType:isSticker:allowUnfilteredUTIs:target:sizes:commonCapabilities:maxDimension:transcoderUserInfo:representations:isLQMEnabled:completionBlock:"
- "transcodeLocalTransferPayloadData:balloonBundleID:completionBlock:"
- "transcribeAudioForAudioTransferURL:withCompletion:"
- "v100@0:8@16@24@32q40@48@56Q64@72q80B88@?92"
- "v100@0:8@16@24@32{IMPreviewConstraints=d{CGSize=dd}dBBB}40Q80@?88B96"
- "v104@0:8@16@24B32@36q44@52@60Q68@76q84B92@?96"
- "v108@0:8@16@24@32{IMPreviewConstraints=d{CGSize=dd}dBBB}40@80@88@?96B104"
- "v112@0:8@16@24B32@36q44@52@60Q68@76q84B92i96B100@?104"
- "v116@0:8@16@24@32{IMPreviewConstraints=d{CGSize=dd}dBBB}40Q80@88@96@?104B112"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "v44@0:8@16@24@32B40"
- "v48@0:8@16@24@32@?40"
- "v52@0:8@16@24@32@?40B48"
- "v56@0:8@16@24@32@40@?48"
- "v60@0:8@16@24@32Q40@?48B56"
- "v60@0:8@16@24@32Q40B48@?52"
- "v72@0:8@16{IMPreviewConstraints=d{CGSize=dd}dBBB}24@?64"
- "v76@0:8@16{IMPreviewConstraints=d{CGSize=dd}dBBB}24i64@?68"
- "v88@0:8@16@24@32{IMPreviewConstraints=d{CGSize=dd}dBBB}40@?80"
- "v92@0:8@16@24@32{IMPreviewConstraints=d{CGSize=dd}dBBB}40@?80B88"
- "valueWithBytes:objCType:"

```
