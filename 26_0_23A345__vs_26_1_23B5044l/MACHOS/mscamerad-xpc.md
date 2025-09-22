## mscamerad-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/mscamerad-xpc.xpc/mscamerad-xpc`

```diff

-2019.0.0.0.0
-  __TEXT.__text: 0x21c14
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_stubs: 0x3ce0
-  __TEXT.__objc_methlist: 0x1bec
-  __TEXT.__const: 0x4c
-  __TEXT.__gcc_except_tab: 0x7a8
-  __TEXT.__objc_methname: 0x4d9c
-  __TEXT.__cstring: 0x30c6
-  __TEXT.__oslogstring: 0x80
-  __TEXT.__objc_classname: 0x23a
-  __TEXT.__objc_methtype: 0x9b2
-  __TEXT.__ustring: 0x28e
-  __TEXT.__unwind_info: 0x628
-  __DATA_CONST.__auth_got: 0x550
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__const: 0x708
-  __DATA_CONST.__cfstring: 0x3fa0
-  __DATA_CONST.__objc_classlist: 0x78
+2020.1.5.0.0
+  __TEXT.__text: 0x15f70
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_stubs: 0x2d20
+  __TEXT.__objc_methlist: 0xffc
+  __TEXT.__const: 0x3c
+  __TEXT.__gcc_except_tab: 0x200
+  __TEXT.__objc_methname: 0x31e9
+  __TEXT.__cstring: 0x1103
+  __TEXT.__oslogstring: 0x3f
+  __TEXT.__ustring: 0x280
+  __TEXT.__objc_classname: 0x128
+  __TEXT.__objc_methtype: 0x629
+  __TEXT.__unwind_info: 0x398
+  __DATA_CONST.__auth_got: 0x3e8
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__const: 0x430
+  __DATA_CONST.__cfstring: 0x1da0
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__objc_intobj: 0x6f0
-  __DATA_CONST.__objc_arraydata: 0x28b8
-  __DATA_CONST.__objc_dictobj: 0x21c0
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_const: 0x26f0
-  __DATA.__objc_selrefs: 0x14e8
-  __DATA.__objc_ivar: 0x1f4
-  __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x3d0
-  __DATA.__common: 0x28
-  __DATA.__bss: 0x68
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA.__objc_const: 0x14e8
+  __DATA.__objc_selrefs: 0xee0
+  __DATA.__objc_ivar: 0x118
+  __DATA.__objc_data: 0x1e0
+  __DATA.__data: 0x248
+  __DATA.__common: 0x18
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/ImageCaptureDevices.framework/ImageCaptureDevices
   - /System/Library/PrivateFrameworks/MMCS.framework/MMCS
-  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: DCB0B052-B322-379E-997F-172EA0796F88
-  Functions: 621
-  Symbols:   265
-  CStrings:  2129
+  UUID: 9E74E039-B1AC-3C69-9518-225597742D73
+  Functions: 363
+  Symbols:   1141
+  CStrings:  1228
 
Symbols:
+ -[AVAsset(VideoOrientation) decodableVideoNamed:width:height:]
+ -[AVAsset(VideoOrientation) videoOrientation]
+ -[ICBufferCache .cxx_destruct]
+ -[ICBufferCache addSemaphore]
+ -[ICBufferCache availSlots]
+ -[ICBufferCache bufDict]
+ -[ICBufferCache bufferAtSlot:]
+ -[ICBufferCache bytesRead]
+ -[ICBufferCache consumeBufferAtOffset:sized:]
+ -[ICBufferCache consumedOffset]
+ -[ICBufferCache dealloc]
+ -[ICBufferCache dequeueBufferAtOffset:sized:buf:]
+ -[ICBufferCache initWithFile:]
+ -[ICBufferCache initWithFile:].cold.1
+ -[ICBufferCache msFile]
+ -[ICBufferCache opQueue]
+ -[ICBufferCache readLength]
+ -[ICBufferCache readOffset]
+ -[ICBufferCache readQueue]
+ -[ICBufferCache reading]
+ -[ICBufferCache resetBufferAtOffset:]
+ -[ICBufferCache resetBufferAtSlot:]
+ -[ICBufferCache setAddSemaphore:]
+ -[ICBufferCache setAvailSlots:]
+ -[ICBufferCache setBufDict:]
+ -[ICBufferCache setBytesRead:]
+ -[ICBufferCache setConsumedOffset:]
+ -[ICBufferCache setMsFile:]
+ -[ICBufferCache setOpQueue:]
+ -[ICBufferCache setReadLength:]
+ -[ICBufferCache setReadOffset:]
+ -[ICBufferCache setReading:]
+ -[ICBufferCache startReading]
+ -[ICBufferCache stopReading]
+ -[MSCameraDevice .cxx_destruct]
+ -[MSCameraDevice acceptConnection:]
+ -[MSCameraDevice addCameraFileToIndex:]
+ -[MSCameraDevice addCameraFolderToIndex:]
+ -[MSCameraDevice beingEjected]
+ -[MSCameraDevice cameraFileWithObjectID:]
+ -[MSCameraDevice cameraFolderWithObjectID:]
+ -[MSCameraDevice cameraItemWithObjectID:]
+ -[MSCameraDevice cameraViewfinder:viewfinderSessionDidBegin:]
+ -[MSCameraDevice cameraViewfinder:viewfinderSessionDidEnd:]
+ -[MSCameraDevice cameraViewfinderSessionDidFinishMovieRecording:]
+ -[MSCameraDevice cameraViewfinderSessionDidStartMovieRecording:]
+ -[MSCameraDevice catalogingDone]
+ -[MSCameraDevice closeDevice]
+ -[MSCameraDevice copyIndexedFoldersAndFilesURLs]
+ -[MSCameraDevice copyIndexedFoldersAndFiles]
+ -[MSCameraDevice dealloc]
+ -[MSCameraDevice deleteFile:]
+ -[MSCameraDevice eject]
+ -[MSCameraDevice enumerateContentWithOptions:]
+ -[MSCameraDevice enumeratedItemCount]
+ -[MSCameraDevice filesystemPath]
+ -[MSCameraDevice filledStorageCache]
+ -[MSCameraDevice incrementPreflightObjectCount:]
+ -[MSCameraDevice indexedFiles]
+ -[MSCameraDevice indexedFolders]
+ -[MSCameraDevice indexedMediaSet]
+ -[MSCameraDevice initWithDeviceContext:]
+ -[MSCameraDevice itemsInFolder:]
+ -[MSCameraDevice mediaPaths]
+ -[MSCameraDevice movieRecording]
+ -[MSCameraDevice name]
+ -[MSCameraDevice notifyDeviceReadyObjectCount]
+ -[MSCameraDevice notifyDeviceReadyPreflightCount]
+ -[MSCameraDevice pauseReflight]
+ -[MSCameraDevice preflight:]
+ -[MSCameraDevice preflightCount]
+ -[MSCameraDevice preflight]
+ -[MSCameraDevice prioritizeSpeed]
+ -[MSCameraDevice reflight:error:]
+ -[MSCameraDevice reflight:error:].cold.1
+ -[MSCameraDevice reflightPauseSource]
+ -[MSCameraDevice reflightPaused]
+ -[MSCameraDevice reflight]
+ -[MSCameraDevice removeCameraFileFromIndex:]
+ -[MSCameraDevice removeCameraFolderFromIndex:]
+ -[MSCameraDevice removeCameraItemFromIndex:]
+ -[MSCameraDevice requestDeleteObjectHandle:options:withReply:]
+ -[MSCameraDevice requestDownloadObjectHandle:options:withReply:]
+ -[MSCameraDevice requestFingerprintForObjectHandle:withReply:]
+ -[MSCameraDevice requestMetadataForObjectHandle:options:withReply:]
+ -[MSCameraDevice requestReadDataFromObjectHandle:options:withReply:]
+ -[MSCameraDevice requestRefreshObjectHandleInfo:withReply:]
+ -[MSCameraDevice requestSecurityScopedURLForObjectHandle:withReply:]
+ -[MSCameraDevice requestStartUsingDeviceWithReply:]
+ -[MSCameraDevice requestThumbnailDataForObjectHandle:options:withReply:]
+ -[MSCameraDevice sendContentsNotification:]
+ -[MSCameraDevice sessionManagerDidCloseAllSessions:]
+ -[MSCameraDevice setCatalogingDone:]
+ -[MSCameraDevice setFilledStorageCache:]
+ -[MSCameraDevice setIndexedMediaSet:]
+ -[MSCameraDevice setMediaPaths:]
+ -[MSCameraDevice setMovieRecording:]
+ -[MSCameraDevice setPreflightCount:]
+ -[MSCameraDevice setPrioritizeSpeed:]
+ -[MSCameraDevice setReflightPauseSource:]
+ -[MSCameraDevice setUrl:]
+ -[MSCameraDevice setViewFinder:]
+ -[MSCameraDevice setViewFinderDelegateQueue:]
+ -[MSCameraDevice setViewFinderOpen:]
+ -[MSCameraDevice updateCatalogingDone]
+ -[MSCameraDevice updateEnumeratedItemCountWithDelta:]
+ -[MSCameraDevice url]
+ -[MSCameraDevice viewFinderDelegateQueue]
+ -[MSCameraDevice viewFinderOpen]
+ -[MSCameraDevice viewFinder]
+ -[MSCameraFile .cxx_destruct]
+ -[MSCameraFile UTI]
+ -[MSCameraFile addSubImageDict:]
+ -[MSCameraFile bitsPerPixel]
+ -[MSCameraFile bufferCache]
+ -[MSCameraFile clearDevice]
+ -[MSCameraFile closeMap:size:]
+ -[MSCameraFile closeStream]
+ -[MSCameraFile compare:against:withContext:]
+ -[MSCameraFile createBufferCache]
+ -[MSCameraFile createImageDataForMaxPixelSize:]
+ -[MSCameraFile createThumbnailUsingOffsets:]
+ -[MSCameraFile dealloc]
+ -[MSCameraFile decrementStreamCount]
+ -[MSCameraFile destroyBufferCache]
+ -[MSCameraFile exifThumbOffsets]
+ -[MSCameraFile fileOpenCount]
+ -[MSCameraFile fileOpenLock]
+ -[MSCameraFile fingerprintWithError:]
+ -[MSCameraFile fingerprint]
+ -[MSCameraFile fullMetadata]
+ -[MSCameraFile hasMetadata]
+ -[MSCameraFile hasThumbnail]
+ -[MSCameraFile hasValidInformation:]
+ -[MSCameraFile imageHeight]
+ -[MSCameraFile imageIOSupported]
+ -[MSCameraFile imageIOSupported].cold.1
+ -[MSCameraFile imageOrientation]
+ -[MSCameraFile imageThumbnailDataForMaxPixelSize:rotated:]
+ -[MSCameraFile imageWidth]
+ -[MSCameraFile incrementStreamCount]
+ -[MSCameraFile initForReadingOnlyWithName:parent:device:]
+ -[MSCameraFile initWithFSURL:name:parent:device:fullMetadata:]
+ -[MSCameraFile mediaItemType]
+ -[MSCameraFile metadataDict]
+ -[MSCameraFile metadataWithOptions:reply:]
+ -[MSCameraFile movieThumbnailDataForMaxPixelSize:]
+ -[MSCameraFile openStream]
+ -[MSCameraFile previewThumbnail]
+ -[MSCameraFile processMetadata:]
+ -[MSCameraFile rawImageMinimumProperties]
+ -[MSCameraFile rawImageSupported]
+ -[MSCameraFile rawImageSupported].cold.1
+ -[MSCameraFile rawImageValidateSubImage:error:]
+ -[MSCameraFile readDataWithOptions:reply:]
+ -[MSCameraFile readMap:offset:]
+ -[MSCameraFile readStream:size:offset:]
+ -[MSCameraFile releaseProvider]
+ -[MSCameraFile scaleData:maxPixelSize:]
+ -[MSCameraFile setBitsPerPixel:]
+ -[MSCameraFile setBufferCache:]
+ -[MSCameraFile setFileOpenCount:]
+ -[MSCameraFile setFileOpenLock:]
+ -[MSCameraFile setFingerprint:]
+ -[MSCameraFile setFullMetadata:]
+ -[MSCameraFile setHasMetadata:]
+ -[MSCameraFile setHasThumbnail:]
+ -[MSCameraFile setImageHeight:]
+ -[MSCameraFile setImageOrientation:]
+ -[MSCameraFile setImageWidth:]
+ -[MSCameraFile setPreviewThumbnail:]
+ -[MSCameraFile setSizeAndOrientationFromImageProperties:]
+ -[MSCameraFile setSmallThumbnail:]
+ -[MSCameraFile setSubImages:]
+ -[MSCameraFile setThumbHeight:]
+ -[MSCameraFile setThumbOffset:]
+ -[MSCameraFile setThumbSize:]
+ -[MSCameraFile setThumbWidth:]
+ -[MSCameraFile setUTI:]
+ -[MSCameraFile setUpdatedBasicMetadata:]
+ -[MSCameraFile setUpdatedExpensiveMetadata:]
+ -[MSCameraFile smallThumbnail]
+ -[MSCameraFile subImageDictForPixelWidth:]
+ -[MSCameraFile subImages]
+ -[MSCameraFile thumbHeight]
+ -[MSCameraFile thumbOffset]
+ -[MSCameraFile thumbSize]
+ -[MSCameraFile thumbWidth]
+ -[MSCameraFile thumbnailDataForMaxPixelSize:rotated:]
+ -[MSCameraFile thumbnailDataUsingSidecarFiles]
+ -[MSCameraFile thumbnailDataUsingSidecarFiles].cold.1
+ -[MSCameraFile thumbnailDataWithOptions:reply:]
+ -[MSCameraFile updateBasicMetadata]
+ -[MSCameraFile updatedBasicMetadata]
+ -[MSCameraFile updatedExpensiveMetadata]
+ -[MSCameraFile validateReturnDataSize:forRequestSize:]
+ -[MSCameraFolder .cxx_destruct]
+ -[MSCameraFolder cancelReflight]
+ -[MSCameraFolder clearDevice]
+ -[MSCameraFolder contentIndex]
+ -[MSCameraFolder content]
+ -[MSCameraFolder createAssetFromURL:notify:preflight:]
+ -[MSCameraFolder createValidAssetFromURL:attemptCount:notify:preflight:]
+ -[MSCameraFolder dealloc]
+ -[MSCameraFolder enumerateContentWithOptions:]
+ -[MSCameraFolder folderMatchingPath:]
+ -[MSCameraFolder initWithFSURL:name:parent:device:]
+ -[MSCameraFolder issueReflight]
+ -[MSCameraFolder mediaItemType]
+ -[MSCameraFolder newItemWithFSURL:name:notify:fullMetadata:]
+ -[MSCameraFolder reflightCount]
+ -[MSCameraFolder reflightQueue]
+ -[MSCameraFolder reflightRequested]
+ -[MSCameraFolder reflightSync]
+ -[MSCameraFolder reflightTimer]
+ -[MSCameraFolder setReflightCount:]
+ -[MSCameraFolder setReflightQueue:]
+ -[MSCameraFolder setReflightRequested:]
+ -[MSCameraFolder setReflightTimer:]
+ -[MSCameraFolder validAVAsset:]
+ -[MSCameraItem .cxx_destruct]
+ -[MSCameraItem baseName]
+ -[MSCameraItem cameraItemProxy]
+ -[MSCameraItem cancelSource]
+ -[MSCameraItem captureDate]
+ -[MSCameraItem compareObjectHandle:]
+ -[MSCameraItem dealloc]
+ -[MSCameraItem device]
+ -[MSCameraItem exifCreationDateTime]
+ -[MSCameraItem exifCreationDate]
+ -[MSCameraItem exifModificationDateTime]
+ -[MSCameraItem exifModificationDate]
+ -[MSCameraItem fd]
+ -[MSCameraItem filesystemChangeDescriptor]
+ -[MSCameraItem filesystemChangeSource]
+ -[MSCameraItem fsCreationTime]
+ -[MSCameraItem fsModificationTime]
+ -[MSCameraItem fsSN]
+ -[MSCameraItem initWithFSURL:name:parent:device:]
+ -[MSCameraItem initWithName:parent:device:]
+ -[MSCameraItem locked]
+ -[MSCameraItem mediaItemType]
+ -[MSCameraItem metadata]
+ -[MSCameraItem modificationDate]
+ -[MSCameraItem name]
+ -[MSCameraItem objHandle]
+ -[MSCameraItem parentIndex]
+ -[MSCameraItem parentObject]
+ -[MSCameraItem parent]
+ -[MSCameraItem path]
+ -[MSCameraItem protectionStatus]
+ -[MSCameraItem refreshAndNotify]
+ -[MSCameraItem refreshInfo:]
+ -[MSCameraItem setCameraItemProxy:]
+ -[MSCameraItem setCaptureDate:]
+ -[MSCameraItem setDevice:]
+ -[MSCameraItem setExifCreationDate:]
+ -[MSCameraItem setExifCreationDateTime:]
+ -[MSCameraItem setExifModificationDate:]
+ -[MSCameraItem setExifModificationDateTime:]
+ -[MSCameraItem setFd:]
+ -[MSCameraItem setFilesystemChangeDescriptor:]
+ -[MSCameraItem setFilesystemChangeSource:]
+ -[MSCameraItem setFsCreationTime:]
+ -[MSCameraItem setFsModificationTime:]
+ -[MSCameraItem setFsSN:]
+ -[MSCameraItem setMetadata:]
+ -[MSCameraItem setModificationDate:]
+ -[MSCameraItem setName:]
+ -[MSCameraItem setObjHandle:]
+ -[MSCameraItem setParent:]
+ -[MSCameraItem setParentObject:]
+ -[MSCameraItem setPath:]
+ -[MSCameraItem setProtectionStatus:]
+ -[MSCameraItem setSize:]
+ -[MSCameraItem setType:]
+ -[MSCameraItem size]
+ -[MSCameraItem type]
+ -[MSCameraItem unsignedIntegerValue]
+ -[MSRemoteCameraDeviceManager .cxx_destruct]
+ -[MSRemoteCameraDeviceManager dealloc]
+ -[MSRemoteCameraDeviceManager deviceMatchingInfo]
+ -[MSRemoteCameraDeviceManager domainsByURLEnabled]
+ -[MSRemoteCameraDeviceManager ejectDevice:withReply:]
+ -[MSRemoteCameraDeviceManager init]
+ -[MSRemoteCameraDeviceManager monitoringContext]
+ -[MSRemoteCameraDeviceManager mountURLs]
+ -[MSRemoteCameraDeviceManager processAddedURLs:]
+ -[MSRemoteCameraDeviceManager processMountURLs:]
+ -[MSRemoteCameraDeviceManager processRemovedURLs:]
+ -[MSRemoteCameraDeviceManager setDeviceMatchingInfo:]
+ -[MSRemoteCameraDeviceManager setDomainsByURLEnabled:]
+ -[MSRemoteCameraDeviceManager setMonitoringContext:]
+ -[MSRemoteCameraDeviceManager setMountURLs:]
+ -[MSRemoteCameraDeviceManager startMSDeviceNotifications]
+ -[MSRemoteCameraDeviceManager updatedWithAddedMountPoints:andRemovedMountPoints:]
+ -[NSArray(ImageCaptureAdditions) copyGroupIntoDictionary:]
+ -[NSURL(ImageCaptureAdditions) baseNameKey]
+ -[NSURL(ImageCaptureAdditions) baseName]
+ GCC_except_table156
+ GCC_except_table26
+ GCC_except_table4
+ GCC_except_table41
+ GCC_except_table42
+ GCC_except_table44
+ IsSupportedMassStorageCameraVolume.cold.1
+ OBJC_IVAR_$_ICBufferCache._addSemaphore
+ OBJC_IVAR_$_ICBufferCache._availSlots
+ OBJC_IVAR_$_ICBufferCache._bufDict
+ OBJC_IVAR_$_ICBufferCache._bufferCache
+ OBJC_IVAR_$_ICBufferCache._bytesRead
+ OBJC_IVAR_$_ICBufferCache._consumedOffset
+ OBJC_IVAR_$_ICBufferCache._msFile
+ OBJC_IVAR_$_ICBufferCache._opQueue
+ OBJC_IVAR_$_ICBufferCache._readLength
+ OBJC_IVAR_$_ICBufferCache._readOffset
+ OBJC_IVAR_$_ICBufferCache._reading
+ OBJC_IVAR_$_MSCameraDevice._catalogingDone
+ OBJC_IVAR_$_MSCameraDevice._enumeratedCount
+ OBJC_IVAR_$_MSCameraDevice._filledStorageCache
+ OBJC_IVAR_$_MSCameraDevice._indexedMediaSet
+ OBJC_IVAR_$_MSCameraDevice._mediaLock
+ OBJC_IVAR_$_MSCameraDevice._mediaPaths
+ OBJC_IVAR_$_MSCameraDevice._movieRecording
+ OBJC_IVAR_$_MSCameraDevice._preflightCount
+ OBJC_IVAR_$_MSCameraDevice._prioritizeSpeed
+ OBJC_IVAR_$_MSCameraDevice._reflightPauseSource
+ OBJC_IVAR_$_MSCameraDevice._url
+ OBJC_IVAR_$_MSCameraDevice._viewFinder
+ OBJC_IVAR_$_MSCameraDevice._viewFinderDelegateQueue
+ OBJC_IVAR_$_MSCameraDevice._viewFinderOpen
+ OBJC_IVAR_$_MSCameraFile._UTI
+ OBJC_IVAR_$_MSCameraFile._bitsPerPixel
+ OBJC_IVAR_$_MSCameraFile._bufferCache
+ OBJC_IVAR_$_MSCameraFile._fileOpenCount
+ OBJC_IVAR_$_MSCameraFile._fileOpenLock
+ OBJC_IVAR_$_MSCameraFile._fingerprint
+ OBJC_IVAR_$_MSCameraFile._fullMetadata
+ OBJC_IVAR_$_MSCameraFile._hasMetadata
+ OBJC_IVAR_$_MSCameraFile._previewThumbnail
+ OBJC_IVAR_$_MSCameraFile._smallThumbnail
+ OBJC_IVAR_$_MSCameraFile._subImages
+ OBJC_IVAR_$_MSCameraFile._thumbHeight
+ OBJC_IVAR_$_MSCameraFile._thumbOffset
+ OBJC_IVAR_$_MSCameraFile._thumbSize
+ OBJC_IVAR_$_MSCameraFile._thumbWidth
+ OBJC_IVAR_$_MSCameraFile._updatedBasicMetadata
+ OBJC_IVAR_$_MSCameraFile._updatedExpensiveMetadata
+ OBJC_IVAR_$_MSCameraFolder._content
+ OBJC_IVAR_$_MSCameraFolder._contentIndex
+ OBJC_IVAR_$_MSCameraFolder._reflightCount
+ OBJC_IVAR_$_MSCameraFolder._reflightQueue
+ OBJC_IVAR_$_MSCameraFolder._reflightRequested
+ OBJC_IVAR_$_MSCameraFolder._reflightTimer
+ OBJC_IVAR_$_MSCameraItem._cameraItemProxy
+ OBJC_IVAR_$_MSCameraItem._device
+ OBJC_IVAR_$_MSCameraItem._exifCreationDate
+ OBJC_IVAR_$_MSCameraItem._exifCreationDateTime
+ OBJC_IVAR_$_MSCameraItem._exifModificationDate
+ OBJC_IVAR_$_MSCameraItem._exifModificationDateTime
+ OBJC_IVAR_$_MSCameraItem._fd
+ OBJC_IVAR_$_MSCameraItem._filesystemChangeDescriptor
+ OBJC_IVAR_$_MSCameraItem._filesystemChangeSource
+ OBJC_IVAR_$_MSCameraItem._fsCreationTime
+ OBJC_IVAR_$_MSCameraItem._fsModificationTime
+ OBJC_IVAR_$_MSCameraItem._fsSN
+ OBJC_IVAR_$_MSCameraItem._metadata
+ OBJC_IVAR_$_MSCameraItem._parent
+ OBJC_IVAR_$_MSCameraItem._parentIndex
+ OBJC_IVAR_$_MSCameraItem._path
+ OBJC_IVAR_$_MSCameraItem._storageID
+ OBJC_IVAR_$_MSCameraItem._type
+ OBJC_IVAR_$_MSRemoteCameraDeviceManager._deviceMatchingInfo
+ OBJC_IVAR_$_MSRemoteCameraDeviceManager._domainsByURLEnabled
+ OBJC_IVAR_$_MSRemoteCameraDeviceManager._monitoringContext
+ OBJC_IVAR_$_MSRemoteCameraDeviceManager._mountURLs
+ _ICCameraItemProxyTypeFolder
+ _ICGetDimensionsFromImageProperties
+ _ICStandardDateFromString
+ _IsSupportedMassStorageCameraVolume
+ _OBJC_CLASS_$_ICBufferCache
+ _OBJC_CLASS_$_ICCameraFileFingerprint
+ _OBJC_CLASS_$_ICCameraItemProxy
+ _OBJC_CLASS_$_ICOrderedMediaSet
+ _OBJC_CLASS_$_ICRemoteCameraDevice
+ _OBJC_CLASS_$_ICRemoteCameraDeviceManager
+ _OBJC_CLASS_$_MSCameraDevice
+ _OBJC_CLASS_$_MSCameraFile
+ _OBJC_CLASS_$_MSCameraFolder
+ _OBJC_CLASS_$_MSCameraItem
+ _OBJC_CLASS_$_MSRemoteCameraDeviceManager
+ _OBJC_METACLASS_$_ICBufferCache
+ _OBJC_METACLASS_$_ICRemoteCameraDevice
+ _OBJC_METACLASS_$_ICRemoteCameraDeviceManager
+ _OBJC_METACLASS_$_MSCameraDevice
+ _OBJC_METACLASS_$_MSCameraFile
+ _OBJC_METACLASS_$_MSCameraFolder
+ _OBJC_METACLASS_$_MSCameraItem
+ _OBJC_METACLASS_$_MSRemoteCameraDeviceManager
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _ValidDCFObjectName.cold.1
+ _ValidDCFObjectName.cold.2
+ _ValidDCFObjectName.file
+ _ValidDCFObjectName.fileToken
+ _ValidDCFObjectName.folder
+ _ValidDCFObjectName.folderToken
+ __31-[MSCameraDevice pauseReflight]_block_invoke.243
+ __31-[MSCameraFolder issueReflight]_block_invoke.26
+ __31-[MSCameraFolder issueReflight]_block_invoke.30
+ __37-[ICBufferCache resetBufferAtOffset:]_block_invoke.cold.1
+ __43-[MSCameraDevice sendContentsNotification:]_block_invoke.172
+ __46-[MSCameraFolder enumerateContentWithOptions:]_block_invoke.64
+ __48-[MSRemoteCameraDeviceManager processAddedURLs:]_block_invoke.66
+ __50-[MSCameraFile movieThumbnailDataForMaxPixelSize:]_block_invoke.cold.1
+ __57-[MSRemoteCameraDeviceManager startMSDeviceNotifications]_block_invoke.cold.1
+ __62-[MSCameraDevice requestDeleteObjectHandle:options:withReply:]_block_invoke.132
+ __68-[MSCameraDevice requestSecurityScopedURLForObjectHandle:withReply:]_block_invoke.cold.1
+ __OBJC_$_CATEGORY_AVAsset_$_VideoOrientation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_AVAsset_$_VideoOrientation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_ImageCaptureAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSURL_$_ImageCaptureAdditions
+ __OBJC_$_CATEGORY_NSArray_$_ImageCaptureAdditions
+ __OBJC_$_CATEGORY_NSURL_$_ImageCaptureAdditions
+ __OBJC_$_INSTANCE_METHODS_ICBufferCache
+ __OBJC_$_INSTANCE_METHODS_MSCameraDevice
+ __OBJC_$_INSTANCE_METHODS_MSCameraFile
+ __OBJC_$_INSTANCE_METHODS_MSCameraFolder
+ __OBJC_$_INSTANCE_METHODS_MSCameraItem
+ __OBJC_$_INSTANCE_METHODS_MSRemoteCameraDeviceManager
+ __OBJC_$_INSTANCE_VARIABLES_ICBufferCache
+ __OBJC_$_INSTANCE_VARIABLES_MSCameraDevice
+ __OBJC_$_INSTANCE_VARIABLES_MSCameraFile
+ __OBJC_$_INSTANCE_VARIABLES_MSCameraFolder
+ __OBJC_$_INSTANCE_VARIABLES_MSCameraItem
+ __OBJC_$_INSTANCE_VARIABLES_MSRemoteCameraDeviceManager
+ __OBJC_$_PROP_LIST_AVAsset_$_VideoOrientation
+ __OBJC_$_PROP_LIST_ICBufferCache
+ __OBJC_$_PROP_LIST_ICMediaItemProtocol
+ __OBJC_$_PROP_LIST_MSCameraDevice
+ __OBJC_$_PROP_LIST_MSCameraFile
+ __OBJC_$_PROP_LIST_MSCameraFolder
+ __OBJC_$_PROP_LIST_MSCameraItem
+ __OBJC_$_PROP_LIST_MSRemoteCameraDeviceManager
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_NSURL_$_ImageCaptureAdditions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FigCameraViewfinderDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICMediaItemProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICSessionManagerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FigCameraViewfinderDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FigCameraViewfinderSessionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FigCameraViewfinderDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FigCameraViewfinderSessionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICMediaItemProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICSessionManagerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_FigCameraViewfinderDelegate
+ __OBJC_$_PROTOCOL_REFS_FigCameraViewfinderSessionDelegate
+ __OBJC_$_PROTOCOL_REFS_ICSessionManagerProtocol
+ __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_MSCameraDevice
+ __OBJC_CLASS_PROTOCOLS_$_MSCameraItem
+ __OBJC_CLASS_RO_$_ICBufferCache
+ __OBJC_CLASS_RO_$_MSCameraDevice
+ __OBJC_CLASS_RO_$_MSCameraFile
+ __OBJC_CLASS_RO_$_MSCameraFolder
+ __OBJC_CLASS_RO_$_MSCameraItem
+ __OBJC_CLASS_RO_$_MSRemoteCameraDeviceManager
+ __OBJC_LABEL_PROTOCOL_$_FigCameraViewfinderDelegate
+ __OBJC_LABEL_PROTOCOL_$_FigCameraViewfinderSessionDelegate
+ __OBJC_LABEL_PROTOCOL_$_ICMediaItemProtocol
+ __OBJC_LABEL_PROTOCOL_$_ICSessionManagerProtocol
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_METACLASS_RO_$_ICBufferCache
+ __OBJC_METACLASS_RO_$_MSCameraDevice
+ __OBJC_METACLASS_RO_$_MSCameraFile
+ __OBJC_METACLASS_RO_$_MSCameraFolder
+ __OBJC_METACLASS_RO_$_MSCameraItem
+ __OBJC_METACLASS_RO_$_MSRemoteCameraDeviceManager
+ __OBJC_PROTOCOL_$_FigCameraViewfinderDelegate
+ __OBJC_PROTOCOL_$_FigCameraViewfinderSessionDelegate
+ __OBJC_PROTOCOL_$_ICMediaItemProtocol
+ __OBJC_PROTOCOL_$_ICSessionManagerProtocol
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_NSXPCListenerDelegate
+ __ValidDCFObjectName
+ ___26-[ICBufferCache readQueue]_block_invoke
+ ___26-[MSCameraDevice reflight]_block_invoke
+ ___26-[MSCameraDevice reflight]_block_invoke_2
+ ___28-[ICBufferCache stopReading]_block_invoke
+ ___28-[MSCameraFile metadataDict]_block_invoke
+ ___28-[MSCameraItem refreshInfo:]_block_invoke
+ ___29-[ICBufferCache startReading]_block_invoke
+ ___30-[MSCameraFolder reflightSync]_block_invoke
+ ___30-[MSCameraFolder reflightSync]_block_invoke_2
+ ___31-[MSCameraDevice pauseReflight]_block_invoke
+ ___31-[MSCameraFolder issueReflight]_block_invoke
+ ___31-[MSCameraFolder issueReflight]_block_invoke_2
+ ___31-[MSCameraFolder validAVAsset:]_block_invoke
+ ___32-[MSCameraFile imageIOSupported]_block_invoke
+ ___33-[MSCameraFile rawImageSupported]_block_invoke
+ ___37-[ICBufferCache resetBufferAtOffset:]_block_invoke
+ ___43-[MSCameraDevice sendContentsNotification:]_block_invoke
+ ___45-[AVAsset(VideoOrientation) videoOrientation]_block_invoke
+ ___45-[ICBufferCache consumeBufferAtOffset:sized:]_block_invoke
+ ___46-[MSCameraFolder enumerateContentWithOptions:]_block_invoke
+ ___46-[MSCameraFolder enumerateContentWithOptions:]_block_invoke_2
+ ___48-[MSRemoteCameraDeviceManager processAddedURLs:]_block_invoke
+ ___49-[ICBufferCache dequeueBufferAtOffset:sized:buf:]_block_invoke
+ ___50-[MSCameraFile movieThumbnailDataForMaxPixelSize:]_block_invoke
+ ___51-[MSCameraDevice requestStartUsingDeviceWithReply:]_block_invoke
+ ___51-[MSCameraFolder initWithFSURL:name:parent:device:]_block_invoke
+ ___51-[MSCameraFolder initWithFSURL:name:parent:device:]_block_invoke_2
+ ___57-[MSRemoteCameraDeviceManager startMSDeviceNotifications]_block_invoke
+ ___59-[MSCameraDevice requestRefreshObjectHandleInfo:withReply:]_block_invoke
+ ___62-[AVAsset(VideoOrientation) decodableVideoNamed:width:height:]_block_invoke
+ ___62-[MSCameraDevice requestDeleteObjectHandle:options:withReply:]_block_invoke
+ ___62-[MSCameraDevice requestFingerprintForObjectHandle:withReply:]_block_invoke
+ ___62-[MSCameraFile initWithFSURL:name:parent:device:fullMetadata:]_block_invoke
+ ___64-[MSCameraDevice requestDownloadObjectHandle:options:withReply:]_block_invoke
+ ___67-[MSCameraDevice requestMetadataForObjectHandle:options:withReply:]_block_invoke
+ ___68-[MSCameraDevice requestReadDataFromObjectHandle:options:withReply:]_block_invoke
+ ___68-[MSCameraDevice requestSecurityScopedURLForObjectHandle:withReply:]_block_invoke
+ ___72-[MSCameraDevice requestThumbnailDataForObjectHandle:options:withReply:]_block_invoke
+ ___72-[MSCameraFolder createValidAssetFromURL:attemptCount:notify:preflight:]_block_invoke
+ ___72-[MSCameraFolder createValidAssetFromURL:attemptCount:notify:preflight:]_block_invoke_2
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___ICLogTypeEnabled
+ ___ICOSLogCreate
+ ____ValidDCFObjectName_block_invoke
+ ____ValidDCFObjectName_block_invoke_2
+ ___block_descriptor_32_e28_"<NSCopying>"16?0"NSURL"8l
+ ___block_descriptor_32_e35_"<NSCopying>"16?0"MSCameraItem"8l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_36_e5_v8?0l
+ ___block_descriptor_40_e25_q24?0"NSURL"8"NSURL"16l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e29_v24?0"NSArray"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e53_v80?0{?=qiIq}8^{CGImage=}32{?=qiIq}40q64"NSError"72lr48l8s32l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_72_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_88_e8_32s40s48r56r64r_e29_v24?0"NSArray"8"NSError"16lr48l8r56l8r64l8s32l8s40l8
+ ___block_literal_global
+ __block_literal_global.3
+ __block_literal_global.489
+ __block_literal_global.492
+ __gBenchmarkStartMachTime
+ __gICOSLog
+ __gLastBenchmarkElapsedMilliseconds
+ __gPTPImageIOSupportedFileExtensions
+ __gPTPKnownRawExtensions
+ __sCameraFileID
+ _main
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$UTF8String
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$addCameraFileToIndex:
+ _objc_msgSend$addCameraFolderToIndex:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addInitiatedOperation:
+ _objc_msgSend$addInteractiveOperation:
+ _objc_msgSend$addMediaItemToIndex:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addSemaphore
+ _objc_msgSend$addSubImageDict:
+ _objc_msgSend$allConnections
+ _objc_msgSend$allKeys
+ _objc_msgSend$allObjects
+ _objc_msgSend$array
+ _objc_msgSend$arrayForType:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$auditToken
+ _objc_msgSend$availSlots
+ _objc_msgSend$baseNameKey
+ _objc_msgSend$beginMonitoringProviderDomainChangesWithHandler:
+ _objc_msgSend$beingEjected
+ _objc_msgSend$blockOperationWithBlock:
+ _objc_msgSend$boolValue
+ _objc_msgSend$bufDict
+ _objc_msgSend$bufferAtSlot:
+ _objc_msgSend$bufferCache
+ _objc_msgSend$bytes
+ _objc_msgSend$cameraDictionary
+ _objc_msgSend$cameraFileWithObjectID:
+ _objc_msgSend$cameraFolderWithObjectID:
+ _objc_msgSend$cameraItemProxy
+ _objc_msgSend$cameraItemWithObjectID:
+ _objc_msgSend$cancelAllOperations
+ _objc_msgSend$cancelReflight
+ _objc_msgSend$cancelSource
+ _objc_msgSend$captureDate
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$clearDevice
+ _objc_msgSend$closeStream
+ _objc_msgSend$code
+ _objc_msgSend$commonKey
+ _objc_msgSend$commonMetadata
+ _objc_msgSend$conformsToType:
+ _objc_msgSend$consumeBufferAtOffset:sized:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$containsString:
+ _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
+ _objc_msgSend$copy
+ _objc_msgSend$copyGroupIntoDictionary:
+ _objc_msgSend$copyIndexedFoldersAndFilesURLs
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createAssetFromURL:notify:preflight:
+ _objc_msgSend$createBufferCache
+ _objc_msgSend$createImageDataForMaxPixelSize:
+ _objc_msgSend$createThumbnailUsingOffsets:
+ _objc_msgSend$createValidAssetFromURL:attemptCount:notify:preflight:
+ _objc_msgSend$currentConnection
+ _objc_msgSend$currentRunLoop
+ _objc_msgSend$data
+ _objc_msgSend$dateFromString:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$decodableVideoNamed:width:height:
+ _objc_msgSend$decrementStreamCount
+ _objc_msgSend$defaultManager
+ _objc_msgSend$deleteFile:
+ _objc_msgSend$description
+ _objc_msgSend$destroyBufferCache
+ _objc_msgSend$device
+ _objc_msgSend$deviceMatchingInfo
+ _objc_msgSend$deviceOperationQueue
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$domainsByURLEnabled
+ _objc_msgSend$duration
+ _objc_msgSend$endMonitoringProviderDomainChanges:
+ _objc_msgSend$enumerateContentWithOptions:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$exifCreationDateTime
+ _objc_msgSend$exifModificationDateTime
+ _objc_msgSend$fd
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$filesystemChangeDescriptor
+ _objc_msgSend$filesystemChangeSource
+ _objc_msgSend$filledStorageCache
+ _objc_msgSend$fingerprint
+ _objc_msgSend$fingerprintForFileAtURL:error:
+ _objc_msgSend$fingerprintWithError:
+ _objc_msgSend$firstObject
+ _objc_msgSend$floatValue
+ _objc_msgSend$folderMatchingPath:
+ _objc_msgSend$formatDescriptions
+ _objc_msgSend$fullMetadata
+ _objc_msgSend$generateCGImagesAsynchronouslyForTimes:completionHandler:
+ _objc_msgSend$getBytes:maxLength:usedLength:encoding:options:range:remainingRange:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$hasMetadata
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$hasThumbnail
+ _objc_msgSend$hasValidInformation:
+ _objc_msgSend$height
+ _objc_msgSend$holdPowerAssertion
+ _objc_msgSend$identifier
+ _objc_msgSend$imageHeight
+ _objc_msgSend$imageIOSupported
+ _objc_msgSend$imageOrientation
+ _objc_msgSend$imageThumbnailDataForMaxPixelSize:rotated:
+ _objc_msgSend$imageWidth
+ _objc_msgSend$incrementPreflightObjectCount:
+ _objc_msgSend$incrementStreamCount
+ _objc_msgSend$indexedFiles
+ _objc_msgSend$indexedFolders
+ _objc_msgSend$indexedMediaSet
+ _objc_msgSend$initForReadingOnlyWithName:parent:device:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithAsset:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithContentsOfFile:
+ _objc_msgSend$initWithContentsOfURL:
+ _objc_msgSend$initWithFSURL:name:parent:device:
+ _objc_msgSend$initWithFSURL:name:parent:device:fullMetadata:
+ _objc_msgSend$initWithFile:
+ _objc_msgSend$initWithLength:
+ _objc_msgSend$initWithTypes:
+ _objc_msgSend$initWithURL:options:
+ _objc_msgSend$initWithURL:readonly:scope:
+ _objc_msgSend$intValue
+ _objc_msgSend$integerValue
+ _objc_msgSend$invalidate
+ _objc_msgSend$isDecodable
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$issueReflight
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$length
+ _objc_msgSend$listener
+ _objc_msgSend$loadTracksWithMediaType:completionHandler:
+ _objc_msgSend$loadValuesAsynchronouslyForKeys:completionHandler:
+ _objc_msgSend$locked
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$mediaItemCount
+ _objc_msgSend$mediaItemWithHandle:inTypes:
+ _objc_msgSend$mediaPaths
+ _objc_msgSend$metadata
+ _objc_msgSend$metadataDict
+ _objc_msgSend$metadataWithOptions:reply:
+ _objc_msgSend$minusSet:
+ _objc_msgSend$modificationDate
+ _objc_msgSend$mountURLs
+ _objc_msgSend$movieRecording
+ _objc_msgSend$movieThumbnailDataForMaxPixelSize:
+ _objc_msgSend$msFile
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$name
+ _objc_msgSend$newItemWithFSURL:name:notify:fullMetadata:
+ _objc_msgSend$notifyClientDeviceAdded:uuidString:deviceName:
+ _objc_msgSend$notifyClientDeviceRemoved:
+ _objc_msgSend$notifyDeviceReadyObjectCount
+ _objc_msgSend$notifyDeviceReadyPreflightCount
+ _objc_msgSend$numberOfMatchesInString:options:range:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objHandle
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$objectHandle
+ _objc_msgSend$openStream
+ _objc_msgSend$orientation
+ _objc_msgSend$parent
+ _objc_msgSend$parentObjectHandle
+ _objc_msgSend$path
+ _objc_msgSend$pathComponents
+ _objc_msgSend$pathExtension
+ _objc_msgSend$pathWithComponents:
+ _objc_msgSend$pauseReflight
+ _objc_msgSend$performSelector:onTypes:
+ _objc_msgSend$preferredTransform
+ _objc_msgSend$preflight
+ _objc_msgSend$preflight:
+ _objc_msgSend$preflightCount
+ _objc_msgSend$prioritizeSpeed
+ _objc_msgSend$processAddedURLs:
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$processMetadata:
+ _objc_msgSend$processMountURLs:
+ _objc_msgSend$processRemovedURLs:
+ _objc_msgSend$protectionStatus
+ _objc_msgSend$providerDisplayName
+ _objc_msgSend$providerDomainForURL:error:
+ _objc_msgSend$rawImageMinimumProperties
+ _objc_msgSend$rawImageSupported
+ _objc_msgSend$rawImageValidateSubImage:error:
+ _objc_msgSend$readDataWithOptions:reply:
+ _objc_msgSend$readOffset
+ _objc_msgSend$readOnly
+ _objc_msgSend$readQueue
+ _objc_msgSend$readStream:size:offset:
+ _objc_msgSend$reading
+ _objc_msgSend$reflight
+ _objc_msgSend$reflight:error:
+ _objc_msgSend$reflightCount
+ _objc_msgSend$reflightPauseSource
+ _objc_msgSend$reflightPaused
+ _objc_msgSend$reflightQueue
+ _objc_msgSend$reflightRequested
+ _objc_msgSend$reflightTimer
+ _objc_msgSend$refreshInfo:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$releasePowerAssertion
+ _objc_msgSend$removeCameraFileFromIndex:
+ _objc_msgSend$removeCameraFolderFromIndex:
+ _objc_msgSend$removeCameraItemFromIndex:
+ _objc_msgSend$removeMediaItemFromIndex:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$resetBufferAtOffset:
+ _objc_msgSend$resetBufferAtSlot:
+ _objc_msgSend$resourceValuesForKeys:error:
+ _objc_msgSend$resume
+ _objc_msgSend$run
+ _objc_msgSend$scaleData:maxPixelSize:
+ _objc_msgSend$sendAddedItemsNotification:toConnections:
+ _objc_msgSend$sendContentsNotification:
+ _objc_msgSend$sendRemovedItemsNotification:toConnections:
+ _objc_msgSend$sendStatusNotification:toConnections:
+ _objc_msgSend$sendUpdatedItemsNotification:toConnections:
+ _objc_msgSend$serviceListener
+ _objc_msgSend$setAppliesPreferredTrackTransform:
+ _objc_msgSend$setCameraItemProxy:
+ _objc_msgSend$setCaptureDate:
+ _objc_msgSend$setCatalogingDone:
+ _objc_msgSend$setConsumedOffset:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setDelegate:queue:
+ _objc_msgSend$setDevice:
+ _objc_msgSend$setExifCreationDate:
+ _objc_msgSend$setExifCreationDateTime:
+ _objc_msgSend$setExifModificationDate:
+ _objc_msgSend$setExifModificationDateTime:
+ _objc_msgSend$setFd:
+ _objc_msgSend$setFilesystemChangeDescriptor:
+ _objc_msgSend$setFilesystemChangeSource:
+ _objc_msgSend$setFilledStorageCache:
+ _objc_msgSend$setFingerprint:
+ _objc_msgSend$setFullMetadata:
+ _objc_msgSend$setHasMetadata:
+ _objc_msgSend$setHasThumbnail:
+ _objc_msgSend$setHeight:
+ _objc_msgSend$setImageHeight:
+ _objc_msgSend$setImageOrientation:
+ _objc_msgSend$setImageWidth:
+ _objc_msgSend$setMaximumSize:
+ _objc_msgSend$setMetadata:
+ _objc_msgSend$setModificationDate:
+ _objc_msgSend$setMountURLs:
+ _objc_msgSend$setMovieRecording:
+ _objc_msgSend$setName:
+ _objc_msgSend$setObjHandle:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setObjectHandle:
+ _objc_msgSend$setOrientation:
+ _objc_msgSend$setParentObject:
+ _objc_msgSend$setParentObjectHandle:
+ _objc_msgSend$setPath:
+ _objc_msgSend$setPreflightCount:
+ _objc_msgSend$setPreviewThumbnail:
+ _objc_msgSend$setPrioritizeSpeed:
+ _objc_msgSend$setProtectionStatus:
+ _objc_msgSend$setReadOffset:
+ _objc_msgSend$setReadOnly:
+ _objc_msgSend$setReading:
+ _objc_msgSend$setReflightCount:
+ _objc_msgSend$setReflightPauseSource:
+ _objc_msgSend$setReflightQueue:
+ _objc_msgSend$setReflightRequested:
+ _objc_msgSend$setReflightTimer:
+ _objc_msgSend$setSize:
+ _objc_msgSend$setSizeAndOrientationFromImageProperties:
+ _objc_msgSend$setSmallThumbnail:
+ _objc_msgSend$setSubImages:
+ _objc_msgSend$setThumbOffset:
+ _objc_msgSend$setThumbSize:
+ _objc_msgSend$setTopLevel:
+ _objc_msgSend$setType:
+ _objc_msgSend$setUTI:
+ _objc_msgSend$setUpdatedBasicMetadata:
+ _objc_msgSend$setUpdatedExpensiveMetadata:
+ _objc_msgSend$setUrl:
+ _objc_msgSend$setViewFinderOpen:
+ _objc_msgSend$setWidth:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$size
+ _objc_msgSend$smallestEncoding
+ _objc_msgSend$sortDescriptorWithKey:ascending:comparator:
+ _objc_msgSend$sortedArrayUsingDescriptors:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$startMSDeviceNotifications
+ _objc_msgSend$startReading
+ _objc_msgSend$startWithOptions:
+ _objc_msgSend$statusOfValueForKey:error:
+ _objc_msgSend$stop
+ _objc_msgSend$stopReading
+ _objc_msgSend$storageURLs
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringValue
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$subImageDictForPixelWidth:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$thumbHeight
+ _objc_msgSend$thumbOffset
+ _objc_msgSend$thumbSize
+ _objc_msgSend$thumbWidth
+ _objc_msgSend$thumbnailDataForMaxPixelSize:rotated:
+ _objc_msgSend$thumbnailDataWithOptions:reply:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$type
+ _objc_msgSend$typeWithFilenameExtension:
+ _objc_msgSend$underlyingQueue
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$updateBasicMetadata
+ _objc_msgSend$updateEnumeratedItemCountWithDelta:
+ _objc_msgSend$updatedBasicMetadata
+ _objc_msgSend$updatedExpensiveMetadata
+ _objc_msgSend$updatedWithAddedMountPoints:andRemovedMountPoints:
+ _objc_msgSend$uppercaseString
+ _objc_msgSend$url
+ _objc_msgSend$validAVAsset:
+ _objc_msgSend$validateReturnDataSize:forRequestSize:
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$valueWithCMTime:
+ _objc_msgSend$videoOrientation
+ _objc_msgSend$viewFinderOpen
+ _objc_msgSend$waitUntilAllOperationsAreFinished
+ _objc_msgSend$width
+ imageIOSupported.onceToken
+ rawImageSupported.onceToken
- _CFErrorCopyDescription
- _CFUserNotificationCreate
- _CFUserNotificationReceiveResponse
- _CPPowerAssertionCreate
- _MMCSSignatureAndSchemeSize
- _MMCSSignatureGeneratorCreateWithBoundaryKey
- _MMCSSignatureGeneratorFinish
- _MMCSSignatureGeneratorUpdate
- _NSClassFromString
- _NSCocoaErrorDomain
- _NSPOSIXErrorDomain
- _NSSelectorFromString
- _NSStringFromSelector
- _NSUnderlyingErrorKey
- _OBJC_CLASS_$_LSApplicationRecord
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSFileHandle
- _OBJC_CLASS_$_NSIndexSet
- _OBJC_CLASS_$_NSMutableIndexSet
- _OBJC_CLASS_$_NSMutableOrderedSet
- _OBJC_CLASS_$_NSOperationQueue
- _OBJC_CLASS_$_NSProcessInfo
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_CLASS_$_NSXPCListenerEndpoint
- _SecTaskCopySigningIdentifier
- _SecTaskCreateWithAuditToken
- __os_feature_enabled_impl
- __os_log_default
- _dispatch_queue_attr_make_with_qos_class
- _exit
- _free
- _kTCCServiceExternalCameraMedia
- _lseek
- _malloc_type_malloc
- _objc_copyWeak
- _objc_initWeak
- _objc_opt_respondsToSelector
- _objc_release_x1
- _objc_retain_x4
- _objc_setProperty_atomic
- _os_log_create
- _os_transaction_create
- _read
- _sqlite3_close
- _sqlite3_exec
- _sqlite3_open
- _tcc_attributed_entity_get_path
- _tcc_authorization_record_get_authorization_value
- _tcc_authorization_record_get_service
- _tcc_authorization_record_get_subject_attributed_entity
- _tcc_authorization_record_get_subject_identity
- _tcc_identity_create
- _tcc_identity_get_identifier
- _tcc_server_create
- _tcc_server_message_get_authorization_records_by_identity
- _tcc_server_message_get_authorization_records_by_service
- _tcc_server_message_set_authorization_value
- _tcc_service_get_name
- _tcc_service_singleton_for_CF_name
- _xpc_bool_get_value
- _xpc_connection_copy_entitlement_value
- _xpc_connection_get_audit_token
- radr://5614542
CStrings:
- ""
- "!"
- "$"
- "%05d-%@"
- "%@ (read) Access State %d, adding"
- "%@ (read) Access State Unknown, not adding"
- "%@ (read) Access State Unknown, not updating"
- "%@ (write) Access State %d, adding"
- "%@ (write) Access State Unknown, not adding"
- "%@ (write) Access State Unknown, not updating"
- "%@ Setting (read) Access State %d"
- "%@ Setting (write) Access State %d"
- "%@ is already in the database, will not be added again"
- "%@-%d"
- "%@-[D]"
- "%@:%@"
- "%s"
- "(check) ---> New kTCCServiceExternalCameraMedia Service"
- "+ %@:[%05lu]"
- "+ note: [%05d] - %@"
- "- %@:[%05lu]"
- "- note: [%05d] - %@"
- "/var/mobile/Library/com.apple.imagecapture"
- "0x%08lX"
- "1"
- "> Existing Device"
- "> New Device: %@"
- "> Not Found: %@"
- "???"
- "@\"<ICSessionManagerProtocol>\""
- "@\"ICRemoteCameraDevice\""
- "@\"ICSessionManager\""
- "@\"NSOperationQueue\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@24@0:8@\"NSCoder\"16"
- "@28@0:8@16B24"
- "@28@0:8i16^@20"
- "@32@0:8Q16@24"
- "B20@0:8i16"
- "B40@0:8@16@24@32"
- "Bundle was not found to be installed on the device, revoking access defensively to require the user to re-authorize upon install."
- "Bundle:%s -- value: %llu"
- "CM"
- "CREATE TABLE IF NOT EXISTS external_device_access (ID INTEGER PRIMARY KEY AUTOINCREMENT, bundle_id TEXT, date_added INTEGER, read_access INTEGER, write_access INTEGER, control_informed INTEGER)"
- "DELETE FROM external_device_access WHERE bundle_id IS '%@';"
- "DEPRECATED"
- "EEXIST"
- "ENOSPC"
- "EPERM"
- "Exiting %@"
- "Failed to close database"
- "Failed to create table: external_device_access - %s"
- "Failed to open/create database"
- "ICAuthorizationBypassEntitlement found"
- "ICCameraDeviceProtocol"
- "ICCameraItemProxy"
- "ICDeviceAccessManager"
- "ICDeviceAccessManagerQueue"
- "ICDeviceContexts"
- "ICDeviceEndpoint"
- "ICDeviceHandle"
- "ICDeviceOperationQueue"
- "ICDeviceUnderlyingQueue"
- "ICInternalDeviceUUID"
- "ICLegacyReturnCodeCannotYieldDevice"
- "ICLegacyReturnCodeCommunicationErr"
- "ICLegacyReturnCodeDataTypeNotFoundErr"
- "ICLegacyReturnCodeDeviceAlreadyOpenErr"
- "ICLegacyReturnCodeDeviceIOServicePathNotFoundErr"
- "ICLegacyReturnCodeDeviceInternalErr"
- "ICLegacyReturnCodeDeviceInvalidParamErr"
- "ICLegacyReturnCodeDeviceLocationIDNotFoundErr"
- "ICLegacyReturnCodeDeviceMemoryAllocationErr"
- "ICLegacyReturnCodeDeviceNotFoundErr"
- "ICLegacyReturnCodeDeviceNotOpenErr"
- "ICLegacyReturnCodeDeviceUnsupportedErr"
- "ICLegacyReturnCodeExtensionInternalErr"
- "ICLegacyReturnCodeFileCorruptedErr"
- "ICLegacyReturnCodeFrameworkInternalErr"
- "ICLegacyReturnCodeIOPendingErr"
- "ICLegacyReturnCodeIndexOutOfRangeErr"
- "ICLegacyReturnCodeInvalidObjectErr"
- "ICLegacyReturnCodeInvalidPropertyErr"
- "ICLegacyReturnCodeInvalidSessionErr"
- "ICLegacyReturnCodePropertyTypeNotFoundErr"
- "ICNotificationTypeDeviceForwardPTPEvents"
- "ICOrderedMediaSet"
- "ICRemoteCameraDevice"
- "ICRemoteCameraDeviceManager"
- "ICRemoteCameraDeviceProxy"
- "ICRemoteManagerAuthorized"
- "ICRemoteManagerConnection"
- "ICReturnCommunicationTimedOut"
- "ICReturnConnectionFailedToOpen"
- "ICReturnDeleteFilesCanceled"
- "ICReturnDeleteFilesFailed"
- "ICReturnDeviceCommandGeneralFailure"
- "ICReturnDeviceCouldNotPair"
- "ICReturnDeviceFailedToCloseSession"
- "ICReturnDeviceFailedToCompleteTransfer"
- "ICReturnDeviceFailedToOpenSession"
- "ICReturnDeviceFailedToSendData"
- "ICReturnDeviceFailedToTakePicture"
- "ICReturnDeviceIsBusyEnumerating"
- "ICReturnDeviceIsPasscodeLocked"
- "ICReturnDeviceNeedsCredentials"
- "ICReturnDeviceSoftwareInstallationCanceled"
- "ICReturnDeviceSoftwareInstallationCompleted"
- "ICReturnDeviceSoftwareInstallationFailed"
- "ICReturnDeviceSoftwareIsBeingInstalled"
- "ICReturnDeviceSoftwareNotAvailable"
- "ICReturnDeviceSoftwareNotInstalled"
- "ICReturnDownloadCanceled"
- "ICReturnDownloadFailed"
- "ICReturnFailedToCompletePassThroughCommand"
- "ICReturnFailedToCompleteSendMessageRequest"
- "ICReturnFailedToDisabeTethering"
- "ICReturnFailedToDisableTethering"
- "ICReturnFailedToEnabeTethering"
- "ICReturnFailedToEnableTethering"
- "ICReturnInvalidParam"
- "ICReturnReceivedUnsolicitedScannerStatusInfo"
- "ICReturnScanOperationCanceled"
- "ICReturnScannerFailedToCompleteOverviewScan"
- "ICReturnScannerFailedToCompleteScan"
- "ICReturnScannerFailedToSelectFunctionalUnit"
- "ICReturnScannerInUseByLocalUser"
- "ICReturnScannerInUseByRemoteUser"
- "ICReturnSessionNotOpened"
- "ICReturnUploadFailed"
- "ICSession"
- "ICSessionManager"
- "ICXPCDeviceManagerProtocol"
- "INSERT INTO external_device_access(bundle_id,date_added,read_access,write_access,control_informed) VALUES ('%@',%lu,%lu,%lu,%lu);"
- "ImageCapture"
- "KERN_NO_ACCESS"
- "MYSUPERSECRECTKEYPADDEDTO32BYTES"
- "NSCoding"
- "NSSecureCoding"
- "New Connection: %d"
- "No work performed in new TCC path"
- "PrivacySettings"
- "Q1"
- "Q32@0:8@16@24"
- "Revoking Application BundleID %@"
- "SELECT bundle_id FROM external_device_access WHERE bundle_id IS '%@';"
- "SELECT bundle_id FROM external_device_access;"
- "SELECT bundle_id, %@ FROM external_device_access;"
- "T@\"<ICSessionManagerProtocol>\",W,N,V_delegate"
- "T@\"ICRemoteCameraDevice\",&,N,V_camera"
- "T@\"ICSessionManager\",&,N,V_sessionManager"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,N"
- "T@\"NSDictionary\",R,N"
- "T@\"NSMutableArray\",&,N,V_addedBundles"
- "T@\"NSMutableArray\",&,N,V_deniedBundles"
- "T@\"NSMutableArray\",&,N,V_remoteCameraDevices"
- "T@\"NSMutableArray\",R,V_notifications"
- "T@\"NSMutableDictionary\",&,N,V_cameraDictionary"
- "T@\"NSMutableDictionary\",&,N,V_keywords"
- "T@\"NSMutableDictionary\",&,N,V_mediaItems"
- "T@\"NSMutableDictionary\",&,N,V_osTransactions"
- "T@\"NSMutableDictionary\",&,N,V_remoteManagerConnections"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_deviceOperationUnderlyingQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_deviceAccessQueue"
- "T@\"NSOperationQueue\",&,N,V_deviceOperationQueue"
- "T@\"NSString\",C,N,V_localizedName"
- "T@\"NSString\",C,N,V_managedObjectName"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_primaryIdentifierString"
- "T@\"NSString\",C,N,V_uuidString"
- "T@\"NSString\",R,N,V_zeroByteFileFingerprint"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"NSXPCListener\",&,N,V_listener"
- "T@\"NSXPCListenerEndpoint\",R"
- "T@,W,N,V_delegate"
- "TB,N,V_hasThumbnail"
- "TB,N,V_readOnly"
- "TB,N,V_systemDaemon"
- "TB,N,V_topLevel"
- "TB,R,N,V_startDeviceNotifications"
- "TB,V_forwardPTPEvents"
- "TB,V_openSession"
- "TCCServiceExternalCameraMedia_iOS"
- "TI,N,V_height"
- "TI,N,V_objectHandle"
- "TI,N,V_orientation"
- "TI,N,V_parentObjectHandle"
- "TI,N,V_sequenceNumber"
- "TI,N,V_storageID"
- "TI,N,V_width"
- "TQ,N,V_captureDate"
- "TQ,N,V_modificationDate"
- "TQ,N,V_size"
- "TQ,R,N,V_sessionCount"
- "TQ,V_objectHandle"
- "T^v,N,V_cpPowerAssertion"
- "T^{sqlite3=},N,V_externalMediaAccessDB"
- "Ti,R,D"
- "T{os_unfair_lock_s=I},N,V_mediaLock"
- "T{os_unfair_lock_s=I},N,V_remoteCameraDevicesLock"
- "T{os_unfair_lock_s=I},N,V_remoteManagerConnectionsLock"
- "UPDATE external_device_access SET %@ = %lu WHERE bundle_id = '%@';"
- "[%05d] - %@"
- "[%05d] --> %@"
- "[IOReturn.h] _device iokit channel busy."
- "[IOReturn.h] _device iokit timeout."
- "[MacErrors.h] _device call unimplemented."
- "[MacErrors.h] _device parameter invalid."
- "[MacErrors.h] _file not found."
- "[MacErrors.h] _scanner has too many clients."
- "[MacErrors.h] _user operation canceled."
- "[errno.h] _device out of space."
- "[errno.h] _file already exists."
- "[errno.h] _file operation not permitted."
- "[kern_return.h] _kernel reurned no access."
- "^^v16@0:8"
- "^v"
- "^v16@0:8"
- "^{sqlite3=}"
- "^{sqlite3=}16@0:8"
- "_addedBundles"
- "_appledevice is locked or unpaired."
- "_appledevice pairing failed."
- "_appledevice unpairing failed."
- "_camera"
- "_camera delete files canceled."
- "_camera delete files failed."
- "_camera disable tethering failed."
- "_camera enable tethering failed."
- "_camera failed to take picture."
- "_camera is enumerating content."
- "_camera passthru command failed."
- "_camera received incorrect data size."
- "_camera send data failed."
- "_cameraDictionary"
- "_captureDate"
- "_connection"
- "_cpPowerAssertion"
- "_createSignatureGenerator"
- "_delegate"
- "_deniedBundles"
- "_device IO Pending."
- "_device already open."
- "_device can't allocate memory."
- "_device close session failed."
- "_device command failed."
- "_device communication error."
- "_device download canceled."
- "_device download failed."
- "_device fw GUID invalid."
- "_device internal error."
- "_device ioservice path invalid."
- "_device module XPC communication failed."
- "_device not found."
- "_device not open."
- "_device open session failed."
- "_device parameter invalid."
- "_device send message failed."
- "_device session invalid."
- "_device session not open."
- "_device unsupported."
- "_device upload failed."
- "_device usb location ID invalid. "
- "_device won't yield."
- "_deviceAccessQueue"
- "_deviceOperationQueue"
- "_deviceOperationUnderlyingQueue"
- "_externalMediaAccessDB"
- "_file corrupted."
- "_forwardPTPEvents"
- "_framework internal error."
- "_hasThumbnail"
- "_height"
- "_keywords"
- "_listener"
- "_localizedName"
- "_lock"
- "_managedObjectName"
- "_mediaItems"
- "_modificationDate"
- "_module communication timed out."
- "_module parameter invalid"
- "_name"
- "_notifications"
- "_object data type not found."
- "_object index out of range."
- "_object invalid."
- "_object property invalid."
- "_object property type invalid."
- "_objectHandle"
- "_obsolete | _device software install canceled."
- "_obsolete | _device software install failed."
- "_obsolete | _device software installed."
- "_obsolete | _device software installing."
- "_obsolete | _device software not available."
- "_obsolete | _device software not installed."
- "_obsoleted"
- "_openSession"
- "_operation success."
- "_orientation"
- "_osTransactions"
- "_parentObjectHandle"
- "_primaryIdentifierString"
- "_readOnly"
- "_remoteCameraDevices"
- "_remoteCameraDevicesLock"
- "_remoteManagerConnections"
- "_remoteManagerConnectionsLock"
- "_resourceLock"
- "_scaner action canceled."
- "_scanner functional unit selection failed."
- "_scanner in use locally."
- "_scanner in use remotely."
- "_scanner overview scan failed."
- "_scanner reported unsolicited error."
- "_scanner reported unsolicited status."
- "_scanner requested scan failed."
- "_sequenceNumber"
- "_sessionConnectionAdded"
- "_sessionCount"
- "_sessionManager"
- "_sessions"
- "_sessionsLock"
- "_size"
- "_startDeviceNotifications"
- "_systemDaemon"
- "_topLevel"
- "_uscandevice needs credentials."
- "_uuidString"
- "_width"
- "_zeroByteFileFingerprint"
- "_zeroByteFileFingerprintOnce"
- "add: [%05d]"
- "addBundleIdentifier:"
- "addNotifications:"
- "addNotifications:toSessionWithConnection:"
- "addOperation:"
- "addRemoteCameraDevice:uuidString:deviceName:"
- "addRemoteManagerConnection:"
- "addSelectorToInterface:selectorString:origin:"
- "addedBundles"
- "additionalProperties"
- "allBundleIdentifiers"
- "anonymousListener"
- "base64EncodedStringWithOptions:"
- "bundleIdentifier:stateForAccessType:"
- "bundleIdentifiersAccessingExternalCameras"
- "bundleIdentifiersAccessingExternalCamerasWithStatus"
- "bundleIdentifiersAccessingExternalCamerasWithStatus: %@"
- "bundleIdentifiersWithAccessType:"
- "bundle_id"
- "camera"
- "captureUserIntentForBundleIdentifier:withNotification:"
- "captureUserIntentForControlWithBundleIdentifier:withNotification:"
- "close device"
- "close: %@"
- "closeDevice:"
- "closeDevice:withReply:"
- "closeFile"
- "com.apple.mscamerad-xpc+%@"
- "com.apple.private.imagecapturecore.authorization_bypass"
- "connection"
- "connection:stateForAccessType:"
- "connections"
- "connectionsMonitoringNotification:"
- "connectionsMonitoringObjectID:"
- "control_informed"
- "count: [%05lu]"
- "cpPowerAssertion"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createSessionWithConnection:"
- "currentSessionCount"
- "dataUsingEncoding:"
- "date"
- "decodeBoolForKey:"
- "decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeObjectOfClass:forKey:"
- "delegate"
- "deniedBundles"
- "deviceAccessQueue"
- "deviceContext"
- "deviceOperationUnderlyingQueue"
- "displayAlertForApplication:withNotification:completionBlock:"
- "displayAlertForControlWithNotification:completionBlock:"
- "domain"
- "encodeBool:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "entity"
- "exists: [%05d]"
- "externalDeviceAccess.db"
- "externalMediaAccessDB"
- "fBsyErr"
- "fileDescriptor"
- "fileExistsAtPath:"
- "fileHandleForReadingFromURL:error:"
- "fingerprintForData:error:"
- "fingerprintForFD:error:"
- "fixupFileHandleError:"
- "fnfErr"
- "forwardPTPEvents"
- "getDeviceList"
- "i24@0:8@16"
- "icaccess"
- "imageCaptureEventNotification:completion:"
- "indexOfObject:inSortedRange:options:usingComparator:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCoder:"
- "initWithConnection:"
- "initWithDelegate:"
- "initWithObjects:"
- "initWithPrimaryIdentifierString:uuidString:localizedName:"
- "insertObject:atIndex:"
- "interestedInNotification:"
- "interfaceWithProtocol:"
- "invalidationHandler"
- "kICASandboxViolation"
- "kICASecureSessionRequired"
- "kIOReturnBusy"
- "kIOReturnTimeout"
- "keywords"
- "legacy"
- "localizedName"
- "longValue"
- "managedObjectName"
- "mediaItems"
- "mediaLock"
- "modern"
- "noteInterest"
- "notifications"
- "notifyAddedDevice:"
- "notifyAddedItems:"
- "notifyDeviceCloseWithUSBLocationID:"
- "notifyPtpEvent:"
- "notifyRemovedDevice:"
- "notifyRemovedItems:"
- "notifyStatus:"
- "notifyUpdatedItems:"
- "objectForKey:"
- "openDB:"
- "openDevice:withReply:"
- "openDeviceSessionWithReply:"
- "openSession"
- "orderedSet"
- "orderedSetForType:"
- "osTransactions"
- "paramErr"
- "pid"
- "postNotification:"
- "primaryIdentifierString"
- "privateBypass"
- "processInfo"
- "processName"
- "ptpEventForwarding:"
- "q24@?0@\"<ICMediaItemProtocol>\"8@\"<ICMediaItemProtocol>\"16"
- "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
- "read_access"
- "registerInterestedEventNotifications:"
- "remNotifications:"
- "remNotifications:fromSessionWithConnection:"
- "remoteCameraDevices"
- "remoteCameraDevicesLock"
- "remoteDeviceForPrimaryIdentifier:"
- "remoteDeviceForUUID:"
- "remoteManager"
- "remoteManagerConnectionWithProcessIdentifierAuthorized:"
- "remoteManagerConnections"
- "remoteManagerConnectionsLock"
- "remoteObjectProxyWithErrorHandler:"
- "remove: [%05lu]"
- "removeAllItems"
- "removeAllObjects"
- "removeAllSessions"
- "removeMediaItemWithHandleFromIndex:"
- "removeMediaItemsFromIndex:"
- "removeObjectsInArray:"
- "removeRemoteCameraDevice:"
- "removeRemoteManagerConnectionWithProcessIdentifier:"
- "removeSessionWithConnection:"
- "removeSessionsWithProcessIdentifier:"
- "requestDeviceListWithOptions:reply"
- "requestDeviceListWithOptions:reply:"
- "requestEjectDeviceWithReply:"
- "revokeBundleIdentifier:"
- "sendNote"
- "sendNotification:toConnections:selector:"
- "sendPTPCommand:andPayload:withReply:"
- "sendPTPEventNotification:"
- "sequenceNumber"
- "sessionCount"
- "sessionManager"
- "sessionWithConnection:"
- "sessions"
- "setAddedBundles:"
- "setCamera:"
- "setCameraDictionary:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConnection:"
- "setCpPowerAssertion:"
- "setDeniedBundles:"
- "setDeviceAccessQueue:"
- "setDeviceOperationQueue:"
- "setDeviceOperationUnderlyingQueue:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExternalMediaAccessDB:"
- "setForwardPTPEvents:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setKeywords:"
- "setListener:"
- "setLocalizedName:"
- "setManagedObjectName:"
- "setMaxConcurrentOperationCount:"
- "setMediaItems:"
- "setMediaLock:"
- "setObject:forKey:"
- "setOpenSession:"
- "setOsTransactions:"
- "setPrimaryIdentifierString:"
- "setQualityOfService:"
- "setQueuePriority:"
- "setRemoteCameraDevices:"
- "setRemoteCameraDevicesLock:"
- "setRemoteManagerConnections:"
- "setRemoteManagerConnectionsLock:"
- "setRemoteObjectInterface:"
- "setSequenceNumber:"
- "setSessionManager:"
- "setStorageID:"
- "setSystemDaemon:"
- "setUnderlyingQueue:"
- "setUuidString:"
- "setWithObjects:"
- "sharedAccessManager"
- "startDeviceNotifications"
- "startListening"
- "storageID"
- "success"
- "supportsSecureCoding"
- "systemDaemon"
- "tcc_server_message_get_authorization_records_by_service error %@"
- "text"
- "topLevel"
- "unimpErr"
- "unregisterInterestedEventNotifications:"
- "updateApplicationWithBundleIdentifier:%@ withStatus:%d"
- "updateApplicationWithBundleIdentifier:withStatus:"
- "updateBundleIdentifier:accessType:withState:"
- "updateRemoteManagerConnectionWithProcessIdentifier:authorized:"
- "userCanceledErr"
- "userInfo"
- "uuidString"
- "v16@?0@\"NSError\"8"
- "v16@?0^{__CFError=}8"
- "v20@?0B8Q12"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSNumber\"16"
- "v24@0:8@?<v@?@\"NSMutableDictionary\">16"
- "v24@0:8^v16"
- "v24@0:8^{sqlite3=}16"
- "v24@0:8i16B20"
- "v24@?0@\"NSObject<OS_tcc_authorization_record>\"8^{__CFError=}16"
- "v28@0:8@16B24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSMutableDictionary\">24"
- "v32@0:8@\"NSMutableDictionary\"16@?<v@?@\"NSMutableDictionary\">24"
- "v32@0:8@\"NSNumber\"16@?<v@?@\"NSMutableDictionary\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSMutableDictionary\">24"
- "v36@0:8@16@24B32"
- "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSMutableDictionary\">32"
- "v40@0:8@\"NSNumber\"16@\"NSDictionary\"24@?<v@?@\"NSMutableDictionary\">32"
- "v40@0:8@16@24:32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24Q32"
- "validateBundleIdentifierInstalled:"
- "value"
- "valueForEntitlement:"
- "whitelisted"
- "write_access"
- "xpc-term: [%05d]"
- "zeroByteFileFingerprint"

```
