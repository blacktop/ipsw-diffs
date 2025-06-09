## mscamerad-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/mscamerad-xpc.xpc/mscamerad-xpc`

```diff

-1936.4.3.0.0
-  __TEXT.__text: 0x20464
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_stubs: 0x3c40
-  __TEXT.__objc_methlist: 0x1b5c
-  __TEXT.__objc_methname: 0x4b94
-  __TEXT.__cstring: 0x2eb7
-  __TEXT.__objc_classname: 0x1e0
-  __TEXT.__objc_methtype: 0x8b0
-  __TEXT.__const: 0x3c
+2013.0.0.0.0
+  __TEXT.__text: 0x204b4
+  __TEXT.__auth_stubs: 0x990
+  __TEXT.__objc_stubs: 0x3cc0
+  __TEXT.__objc_methlist: 0x1bd4
+  __TEXT.__const: 0x44
   __TEXT.__gcc_except_tab: 0x40c
+  __TEXT.__objc_methname: 0x4d22
+  __TEXT.__cstring: 0x2fae
   __TEXT.__oslogstring: 0x3f
+  __TEXT.__objc_classname: 0x23a
+  __TEXT.__objc_methtype: 0x9b2
   __TEXT.__ustring: 0x280
   __TEXT.__unwind_info: 0x5c8
-  __DATA_CONST.__auth_got: 0x4d0
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0x688
-  __DATA_CONST.__cfstring: 0x3c20
+  __DATA_CONST.__auth_got: 0x4d8
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__const: 0x680
+  __DATA_CONST.__cfstring: 0x3ea0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78

   __DATA_CONST.__objc_arraydata: 0x28b8
   __DATA_CONST.__objc_dictobj: 0x21c0
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_const: 0x25c8
-  __DATA.__objc_selrefs: 0x1480
-  __DATA.__objc_ivar: 0x1f0
+  __DATA.__objc_const: 0x26f0
+  __DATA.__objc_selrefs: 0x14d8
+  __DATA.__objc_ivar: 0x1f4
   __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x250
-  __DATA.__bss: 0x68
+  __DATA.__data: 0x3d0
   __DATA.__common: 0x28
+  __DATA.__bss: 0x68
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/MMCS.framework/MMCS
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 2182994A-C436-388A-AD50-D382500200C4
-  Functions: 625
-  Symbols:   246
-  CStrings:  2047
+  UUID: A929AA0E-E707-3BE5-AC07-4ADB9ECCEBBB
+  Functions: 609
+  Symbols:   248
+  CStrings:  2107
 
Symbols:
+ _OBJC_CLASS_$_FigCameraViewfinder
+ _objc_opt_new
+ _usleep
- _CFStringConvertEncodingToNSStringEncoding
CStrings:
+ "6"
+ "@\"FigCameraViewfinder\""
+ "@\"ICCameraItemProxy\""
+ "@24@0:8@\"NSCoder\"16"
+ "FigCameraViewfinderDelegate"
+ "FigCameraViewfinderSessionDelegate"
+ "ICCameraItemProxy"
+ "ICCameraItemProxyArray"
+ "NSCoding"
+ "NSSecureCoding"
+ "Q1"
+ "Reflight Cancelled - enumerating[%d], paused[%d], recording[%d]"
+ "T"
+ "T@\"FigCameraViewfinder\",&,N,V_viewFinder"
+ "T@\"ICCameraItemProxy\",&,N,V_cameraItemProxy"
+ "T@\"NSMutableDictionary\",&,N,V_keywords"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_viewFinderDelegateQueue"
+ "T@\"NSString\",C,N,V_name"
+ "TB,N"
+ "TB,N,V_readOnly"
+ "TB,N,V_topLevel"
+ "TB,V_movieRecording"
+ "TB,V_viewFinderOpen"
+ "TI,N,V_height"
+ "TI,N,V_orientation"
+ "TI,N,V_parentObjectHandle"
+ "TI,N,V_thumbHeight"
+ "TI,N,V_thumbSize"
+ "TI,N,V_thumbWidth"
+ "TI,N,V_width"
+ "TQ,N,V_captureDate"
+ "TQ,N,V_modificationDate"
+ "TQ,N,V_size"
+ "_cameraItemProxy"
+ "_captureDate"
+ "_height"
+ "_keywords"
+ "_modificationDate"
+ "_movieRecording"
+ "_name"
+ "_orientation"
+ "_parentObjectHandle"
+ "_readOnly"
+ "_size"
+ "_thumbHeight"
+ "_thumbSize"
+ "_thumbWidth"
+ "_topLevel"
+ "_viewFinder"
+ "_viewFinderDelegateQueue"
+ "_viewFinderOpen"
+ "_width"
+ "cameraItemProxy"
+ "cameraViewfinder:viewfinderSessionDidBegin:"
+ "cameraViewfinder:viewfinderSessionDidEnd:"
+ "cameraViewfinder:viewfinderSessionWillBegin:"
+ "cameraViewfinderSession:didCapturePhotoWithStatus:thumbnailData:timestamp:"
+ "cameraViewfinderSession:previewStreamDidCloseWithStatus:"
+ "cameraViewfinderSessionDidFinishMovieRecording:"
+ "cameraViewfinderSessionDidStartMovieRecording:"
+ "cameraViewfinderSessionPreviewStreamDidOpen:"
+ "decodeBoolForKey:"
+ "decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:"
+ "decodeInt32ForKey:"
+ "decodeInt64ForKey:"
+ "decodeObjectOfClass:forKey:"
+ "didStart"
+ "didStop"
+ "encodeBool:forKey:"
+ "encodeInt32:forKey:"
+ "encodeInt64:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "height"
+ "initWithCoder:"
+ "keywords"
+ "movieRecording"
+ "orientation"
+ "parentObjectHandle"
+ "readOnly"
+ "setCameraItemProxy:"
+ "setDelegate:queue:"
+ "setHeight:"
+ "setKeywords:"
+ "setMovieRecording:"
+ "setOrientation:"
+ "setParentObjectHandle:"
+ "setReadOnly:"
+ "setSize:"
+ "setTopLevel:"
+ "setViewFinder:"
+ "setViewFinderDelegateQueue:"
+ "setViewFinderOpen:"
+ "setWidth:"
+ "setWithObjects:"
+ "startWithOptions:"
+ "stop"
+ "supportsSecureCoding"
+ "topLevel"
+ "v24@0:8@\"FigCameraViewfinderSession\"16"
+ "v24@0:8@\"NSCoder\"16"
+ "v28@0:8@\"FigCameraViewfinderSession\"16i24"
+ "v28@0:8@16i24"
+ "v32@0:8@\"FigCameraViewfinder\"16@\"FigCameraViewfinderSession\"24"
+ "v60@0:8@\"FigCameraViewfinderSession\"16i24@\"NSData\"28{?=qiIq}36"
+ "v60@0:8@16i24@28{?=qiIq}36"
+ "vfDidEnd"
+ "vfDidStart"
+ "viewFinder"
+ "viewFinderDelegateQueue"
+ "viewFinderOpen"
+ "viewfinder-delegate-queue"
+ "width"
- "4"
- "@\"MSObjectInfoDataset\""
- "@28@0:8*16I24"
- "ICMSObjectInfoArray"
- "MSObjectInfoDataset"
- "Reflight Cancelled - enumerating[%d], paused[%d]"
- "S"
- "S16@0:8"
- "T@\"MSObjectInfoDataset\",&,N,V_info"
- "T@\"NSData\",R,C,N"
- "T@\"NSString\",C,N,V_filename"
- "TI,N,V_associationDesc"
- "TI,N,V_imageBitDepth"
- "TI,N,V_imagePixHeight"
- "TI,N,V_imagePixWidth"
- "TI,N,V_parentObject"
- "TI,N,V_thumbCompressedSize"
- "TI,N,V_thumbPixHeight"
- "TI,N,V_thumbPixWidth"
- "TQ,N,V_captureDate_tvsec"
- "TQ,N,V_ino"
- "TQ,N,V_modificationDate_tvsec"
- "TQ,N,V_objectCompressedSize"
- "TS,N,V_associationType"
- "TS,N,V_imageOrientation"
- "TS,N,V_objectFormat"
- "TS,N,V_protectionStatus"
- "TS,N,V_thumbFormat"
- "_associationDesc"
- "_associationType"
- "_captureDate_tvsec"
- "_filename"
- "_imageBitDepth"
- "_imageOrientation"
- "_imagePixHeight"
- "_imagePixWidth"
- "_info"
- "_ino"
- "_modificationDate_tvsec"
- "_objectCompressedSize"
- "_objectFormat"
- "_parentObject"
- "_protectionStatus"
- "_thumbCompressedSize"
- "_thumbFormat"
- "_thumbPixHeight"
- "_thumbPixWidth"
- "associationDesc"
- "associationType"
- "captureDate_tvsec"
- "contentLength:bufferLength:"
- "fileSize"
- "filename"
- "imageBitDepth"
- "imageData"
- "imagePixHeight"
- "imagePixWidth"
- "info"
- "initWithBytes:length:"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "initWithData:"
- "ino"
- "modificationDate_tvsec"
- "objectCompressedSize"
- "objectFormat"
- "r"
- "setAssociationDesc:"
- "setAssociationType:"
- "setCaptureDate_tvsec:"
- "setFilename:"
- "setImageBitDepth:"
- "setImagePixHeight:"
- "setImagePixWidth:"
- "setInfo:"
- "setIno:"
- "setModificationDate_tvsec:"
- "setObjectCompressedSize:"
- "setObjectFormat:"
- "setThumbCompressedSize:"
- "setThumbFormat:"
- "setThumbPixHeight:"
- "setThumbPixWidth:"
- "thumbCompressedSize"
- "thumbFormat"
- "thumbPixHeight"
- "thumbPixWidth"
- "v20@0:8S16"
- "v32@0:8^I16^I24"
- "\x91"

```
