## WorkflowUI

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI`

```diff

-4607.0.0.0.0
-  __TEXT.__text: 0x2cd760
+4610.0.0.0.0
+  __TEXT.__text: 0x2cd7e4
   __TEXT.__auth_stubs: 0x66e0
   __TEXT.__objc_methlist: 0xd6ac
   __TEXT.__const: 0x1d610

   __TEXT.__swift_as_ret: 0x150
   __TEXT.__gcc_except_tab: 0xcd8
   __TEXT.__ustring: 0x30c
-  __TEXT.__unwind_info: 0xaed8
+  __TEXT.__unwind_info: 0xaed0
   __TEXT.__eh_frame: 0x661c
   __TEXT.__objc_classname: 0x4864
-  __TEXT.__objc_methname: 0x26cc5
-  __TEXT.__objc_methtype: 0x87a4
-  __TEXT.__objc_stubs: 0x18c60
+  __TEXT.__objc_methname: 0x26d15
+  __TEXT.__objc_methtype: 0x87ba
+  __TEXT.__objc_stubs: 0x18c80
   __DATA_CONST.__got: 0x2a18
   __DATA_CONST.__const: 0x23d0
   __DATA_CONST.__objc_classlist: 0x9d0
   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0x580
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8690
+  __DATA_CONST.__objc_selrefs: 0x8698
   __DATA_CONST.__objc_protorefs: 0x1e0
   __DATA_CONST.__objc_superrefs: 0x490
   __DATA_CONST.__objc_arraydata: 0x1d0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4432AD29-EC07-3C6C-8D3E-D980CDFADF8B
+  UUID: CA5C6DF1-826F-36D4-8C6F-21890A80FC64
   Functions: 19613
-  Symbols:   27102
-  CStrings:  9391
+  Symbols:   27103
+  CStrings:  9392
 
Symbols:
+ -[WFLibraryRunCoordinator openWorkflowReferenceAndRun:fromSource:withInput:state:requestOutput:runViewSource:xCallbackURLSuccessURLScheme:completionHandler:]
+ -[WFLibraryRunCoordinator runWorkflowReference:fromSource:withInput:requestOutput:runViewSource:xCallbackURLSuccessURLScheme:completionHandler:]
+ _objc_msgSend$openWorkflowReferenceAndRun:fromSource:withInput:state:requestOutput:runViewSource:xCallbackURLSuccessURLScheme:completionHandler:
+ _objc_msgSend$setXCallbackURLSuccessURLScheme:
- -[WFLibraryRunCoordinator openWorkflowReferenceAndRun:fromSource:withInput:state:requestOutput:runViewSource:completionHandler:]
- -[WFLibraryRunCoordinator runWorkflowReference:fromSource:withInput:requestOutput:runViewSource:completionHandler:]
- _objc_msgSend$openWorkflowReferenceAndRun:fromSource:withInput:state:requestOutput:runViewSource:completionHandler:
CStrings:
+ "openWorkflowReferenceAndRun:fromSource:withInput:state:requestOutput:runViewSource:xCallbackURLSuccessURLScheme:completionHandler:"
+ "runWorkflowReference:fromSource:withInput:requestOutput:runViewSource:xCallbackURLSuccessURLScheme:completionHandler:"
+ "setXCallbackURLSuccessURLScheme:"
+ "v52@?0@\"WFWorkflowReference\"8B16@\"WFContentCollection\"20@?<v@?@\"WFContentCollection\"B@\"NSError\">28@\"NSString\"36@\"NSString\"44"
+ "v68@0:8@16@24@32B40@44@52@?60"
+ "v76@0:8@16@24@32@40B48@52@60@?68"
- "openWorkflowReferenceAndRun:fromSource:withInput:state:requestOutput:runViewSource:completionHandler:"
- "runWorkflowReference:fromSource:withInput:requestOutput:runViewSource:completionHandler:"
- "v44@?0@\"WFWorkflowReference\"8B16@\"WFContentCollection\"20@?<v@?@\"WFContentCollection\"B@\"NSError\">28@\"NSString\"36"
- "v60@0:8@16@24@32B40@44@?52"
- "v68@0:8@16@24@32@40B48@52@?60"

```
