## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1262.400.41.2.3
-  __TEXT.__text: 0x82ed8
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x1f6c
-  __TEXT.__const: 0x198
-  __TEXT.__gcc_except_tab: 0x7c34
-  __TEXT.__cstring: 0x2a4c
-  __TEXT.__oslogstring: 0x1302c
-  __TEXT.__unwind_info: 0x1bb4
-  __TEXT.__objc_classname: 0x47b
-  __TEXT.__objc_methname: 0xe6e0
-  __TEXT.__objc_methtype: 0x2481
-  __TEXT.__objc_stubs: 0xa3c0
-  __DATA_CONST.__got: 0x8a0
-  __DATA_CONST.__const: 0x1fd8
-  __DATA_CONST.__objc_classlist: 0xb8
+1262.500.151.2.4
+  __TEXT.__text: 0x846d4
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_methlist: 0x2064
+  __TEXT.__const: 0x1a8
+  __TEXT.__gcc_except_tab: 0x7d1c
+  __TEXT.__cstring: 0x2afa
+  __TEXT.__oslogstring: 0x13346
+  __TEXT.__unwind_info: 0x1bec
+  __TEXT.__objc_classname: 0x499
+  __TEXT.__objc_methname: 0xedf4
+  __TEXT.__objc_methtype: 0x251d
+  __TEXT.__objc_stubs: 0xa6c0
+  __DATA_CONST.__got: 0x8a8
+  __DATA_CONST.__const: 0x1fe0
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2588
-  __DATA_CONST.__objc_selrefs: 0x2cb8
+  __DATA_CONST.__objc_const: 0x26e8
+  __DATA_CONST.__objc_selrefs: 0x2d78
+  __DATA_CONST.__objc_classrefs: 0x428
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__objc_const: 0x9e0
-  __AUTH_CONST.__const: 0x6a0
-  __AUTH_CONST.__cfstring: 0x3040
+  __AUTH_CONST.__objc_const: 0xa70
+  __AUTH_CONST.__const: 0x6c0
+  __AUTH_CONST.__cfstring: 0x3160
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_classrefs: 0x420
-  __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0x18c
-  __DATA.__data: 0x3b8
-  __DATA.__bss: 0x60
+  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x1a8
+  __DATA.__data: 0x3d8
+  __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__data: 0xc
   __DATA_DIRTY.__bss: 0x58

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A080BC29-C971-304E-AEC8-DC39EA2B667A
-  Functions: 1085
-  Symbols:   665
-  CStrings:  4259
+  UUID: D7B21664-4D5D-3373-9BF8-40376E83B6E7
+  Functions: 1107
+  Symbols:   669
+  CStrings:  4333
 
Symbols:
+ _IMCanonicalizeFormattedString
+ _IMIsSpatialMedia
+ _IMStringIsPhoneNumber
+ _IMUTTypeIsImage
CStrings:
+ "        Was HQ limit: %@"
+ "  Download Restriction Result: %@"
+ " => currentVersion %ld incomingVersion %@"
+ "?1E"
+ "@32@0:8Q16B24B28"
+ "@40@0:8Q16Q24B32B36"
+ "@48@0:8@16Q24Q32B40B44"
+ "@52@0:8@16Q24Q32B40B44B48"
+ "@52@0:8Q16Q24Q32B40B44B48"
+ "AttachmentDownloadRestriction"
+ "B40@0:8@16q24@32"
+ "BIAContext"
+ "Did not generate a message item, bailing early"
+ "Found an inflight request with GUID: %@, incoming GUID: %@"
+ "Generating IMGroupActionItem for group photo update. chatGuid %@ sender %@ fileTransferGuid %@ isHidden %@"
+ "Group photo message parsed: isExplicitlyRequestedResponse: %d, isLegacyRequestedResponse: %d, isExplicitlyNewPhoto: %d, isAssumedLegacyNewPhoto: %d"
+ "IMFoundation"
+ "IMiMessageSizeLimitsForTransferTypeDisableLargeSizeNetworkRestriction"
+ "Incoming group photo participant version (%ld) is newer than local version with last known photo change (%ld), requesting photo"
+ "Overriding file size for spatial image transfer %@"
+ "Received a negative last group photo participant version. This is not right!"
+ "Received group photo update with non-empty fileTransferDict, from %@"
+ "Requesting group photo if necessary. chatGuid %@ incomingParticipantVersion %ld incomingGroupPhotoCreationDate %@ fromStorage %@"
+ "Sending Edited Message with no GUID"
+ "Server bag results for max spatial image %lu default(%@)"
+ "Setting last group photo-related participant version of chat %@ to %ld"
+ "Setting sender to nil (myself) because sender %@ is the lastAddressedLocalHandle or the current account's login ID"
+ "T@\"NSMutableDictionary\",R,N,V_groupPhotoRequestsInFlight"
+ "T@\"NSString\",?,R,C"
+ "TB,R,N,V_allowDownload"
+ "TB,R,N,V_isSticker"
+ "TB,R,N,V_lqmEnabled"
+ "TQ,R,N,V_limitSize"
+ "TQ,R,N,V_limitType"
+ "TQ,R,N,V_qualityType"
+ "The first file wasn't allowed to auto download, let's look and see what we have... shouldAutoDownloadFile %@, lowQualityModeEnabled %@"
+ "Transfer for group photo not yet finalizing %@"
+ "We've already created a status item for this transfer, and the new one is hidden, don't show anything new."
+ "_URIFromCanonicalizedPhoneNumber"
+ "_allowDownload"
+ "_downloadRestrictionForUTIType:fileSize:qualityType:isSticker:forceAutoDownloadIfPossible:lqmEnabled:"
+ "_downloadRestrictionForUTIType:fileSize:qualityType:isSticker:lqmEnabled:"
+ "_fileTransferSizeForSpatialImageFromServerBag:"
+ "_generateAndStoreGroupActionItemForChat passed a nil chat. Early returning"
+ "_generateAndStoreGroupActionItemForChat:sender:"
+ "_groupPhotoRequestsInFlight"
+ "_handleGroupVisualIdentityRequest:fromParticipants:groupID:identifier:session:toIdentifier:fromToken:requestGUID:"
+ "_isSticker"
+ "_limitSize"
+ "_limitType"
+ "_lqmEnabled"
+ "_maxAllowedSpatialImageSize"
+ "_qualityType"
+ "_sendGroupPhoto:toIdentifier:fromIdentifier:toToken:session:requestGUID:"
+ "_shouldRequestGroupPhoto:incomingParticipantVersion:incomingGroupPhotoCreationDate:"
+ "_transcodeURL:reason:transfer:sizes:commonCapabilities:sendStatus:urlGroup:didTranscode:handleURL:"
+ "addBIAContextWithUserID:referenceID:"
+ "allowDownload"
+ "att-spatial-image-max-file-size"
+ "bcon"
+ "chatProperties"
+ "closeSessionForChat:chatGUID:didDeleteConversation:style:"
+ "collectMetricsForDownloadedFile:"
+ "collectMetricsForLimitExceededWithReportedSize:"
+ "dc"
+ "deleteBIAContext"
+ "forceAutoBugCaptureWithSubType:errorPayload:"
+ "gppv"
+ "groupParticipantVersion"
+ "groupPhotoRequestsInFlight"
+ "groupPhotoUploadCompletedForChat:fileTransferGuid:callerURI:fromAccount:message:displayIDs:additionalContext:success:isPhotoRefresh:error:"
+ "im_generateCopyForURL:"
+ "initWithLimitType:limitSize:qualityType:isSticker:allowDownload:lqmEnabled:"
+ "limitSize"
+ "limitType"
+ "lqmEnabled"
+ "ngp"
+ "noSpaceForHighQualityLimit:qualityType:isSticker:lqmEnabled:"
+ "noSpaceForLowQualityLimit:qualityType:isSticker:lqmEnabled:"
+ "qualityType"
+ "requestGroupPhotoIfNecessary:incomingParticipantVersion:incomingGroupPhotoCreationDate:toIdentifier:fromIdentifier:messageIsFromStorage:session:"
+ "requestGroupPhotoIfNecessary:incomingParticipantVersion:incomingGroupPhotoCreationTime:toIdentifier:fromIdentifier:messageIsFromStorage:"
+ "restrictionAllowedBySettingWithQualityType:isSticker:lqmEnabled:"
+ "restrictionDisallowedBySettingWithQualityType:isSticker:lqmEnabled:"
+ "restrictionForceAllowedWithQualityType:isSticker:lqmEnabled:"
+ "restrictionWithLimitType:limitSize:qualityType:isSticker:allowDownload:lqmEnabled:"
+ "retryGroupPhotoUpload:toChatID:identifier:style:account:isPhotoRefresh:"
+ "rg"
+ "rr"
+ "sendGroupPhotoUpdate:toChatID:identifier:style:account:isPhotoRefresh:"
+ "setGroupParticipantVersion:"
+ "setGroupPhoto:forChat:fromID:fromAccount:session:isPhotoRefresh:"
+ "trackAttachmentDownloadLimitExceeded:limitSize:fileSize:qualityType:isSticker:lowQualityModeEnabled:"
+ "trackAttachmentDownloadSuccess:limitType:limitSize:qualityType:isSticker:lowQualityModeEnabled:"
+ "trackiMessageTranscodeFailureWithReason:sourceFile:sizeLimits:isSticker:lowQualityModeEnabled:"
+ "trackiMessageTranscodeWithReason:sourceFile:highQualityFile:lowQualityFile:sizeLimits:isSticker:transcoded:lowQualityModeEnabled:"
+ "uploadGroupPhotoForChat:fileTransferGUID:itemGUID:callerURI:idsAccount:isPhotoRefresh:"
+ "v40@0:8@16@24B32C36"
+ "v56@0:8@16@24@32C40@44B52"
+ "v60@0:8@16q24@32@40@48B56"
+ "v68@0:8@16q24@32@40@48B56@60"
+ "v84@0:8@16@24@32@40@48@56@64B72B76I80"
+ "v88@0:8@16Q24@32@40@48@56@64@?72@?80"
+ "vt"
- "  Result: %@"
- " => currentVersion %d incomingVersion %@"
- "?0E"
- "B32@0:8@16Q24"
- "B36@0:8@16Q24B32"
- "Don't request group photo, incoming group photo is recent enough. Date: %@ "
- "Failed to close session with business URI: %@ Error: %@"
- "Generating IMGroupActionItem for group photo update. chatGuid %@ sender %@ fileTransferGuid %@"
- "Incoming created date %@(%lld) is newer than our existing transfer %@(%lld), request group photo"
- "Received group photo update with non-empty fileTransferDict"
- "Requesting group photo if necessary. chatGuid %@ incomingGroupPhotoCreationDate %@ fromStorage %@"
- "The first file wasn't allowed to auto download, let's look and see what we have... shouldAutoDownloadFile %@, shouldDownloadLowQualityVersion %@"
- "Transfer for group photo not yet finalizaing %@"
- "_generateLinkForURL:"
- "_handleGroupVisualIdentityRequest:fromParticipants:groupID:identifier:session:toIdentifier:fromToken:"
- "_randomTemporaryPathWithFileName:"
- "_sendGroupPhoto:toIdentifier:fromIdentifier:toToken:session:"
- "_shouldAutoDownloadUTIType:fileSize:"
- "_shouldAutoDownloadUTIType:fileSize:shouldForceAutoDownloadIfPossibble:"
- "_shouldRequestGroupPhoto:incomingGroupPhotoCreationDate:"
- "_transcodeURL:transfer:sizes:commonCapabilities:sendStatus:urlGroup:didTranscode:handleURL:"
- "closeSessionChat:style:"
- "didReceiveDisplayNameChange:fromID:toIdentifier:forChat:style:account:sender:"
- "groupPhotoUploadCompletedForChat:fileTransferGuid:callerURI:fromAccount:message:displayIDs:additionalContext:success:error:"
- "laterDate:"
- "pv"
- "requestGroupPhotoIfNecessary:incomingGroupPhotoCreationDate:toIdentifier:fromIdentifier:messageIsFromStorage:session:"
- "requestGroupPhotoIfNecessary:incomingGroupPhotoCreationTime:toIdentifier:fromIdentifier:messageIsFromStorage:"
- "retryGroupPhotoUpload:toChatID:identifier:style:account:"
- "setGroupPhoto:forChat:fromID:fromAccount:session:"
- "updateGroupPhoto:forChat:"
- "updateLastUsedBIAReferenceID:"
- "updateLastUsedBIAUserID:"
- "uploadGroupPhotoForChat:fileTransferGUID:itemGUID:callerURI:idsAccount:"
- "v52@0:8@16@24@32@40B48"
- "v60@0:8@16@24@32@40B48@52"
- "v80@0:8@16@24@32@40@48@56@64B72I76"
- "v80@0:8@16@24@32@40@48@56@?64@?72"
- "writeToFile:options:error:"

```
