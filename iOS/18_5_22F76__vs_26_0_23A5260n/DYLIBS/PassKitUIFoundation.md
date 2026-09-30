## PassKitUIFoundation

> `/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation`

```diff

-1591.6.7.0.0
-  __TEXT.__text: 0x2b780
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x20c4
-  __TEXT.__const: 0x810
-  __TEXT.__cstring: 0x1031
-  __TEXT.__oslogstring: 0x1301
-  __TEXT.__gcc_except_tab: 0x814
-  __TEXT.__unwind_info: 0xb98
+1619.6.3.0.0
+  __TEXT.__text: 0x2844c
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_methlist: 0x1ec4
+  __TEXT.__const: 0x668
+  __TEXT.__cstring: 0xe7a
+  __TEXT.__oslogstring: 0x128e
+  __TEXT.__gcc_except_tab: 0x7ec
+  __TEXT.__unwind_info: 0xac0
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x6bd
-  __TEXT.__objc_methname: 0x7526
-  __TEXT.__objc_methtype: 0x15a8
-  __TEXT.__objc_stubs: 0x60c0
-  __DATA_CONST.__got: 0x580
-  __DATA_CONST.__const: 0x1120
-  __DATA_CONST.__objc_classlist: 0x120
+  __TEXT.__objc_classname: 0x66f
+  __TEXT.__objc_methname: 0x708b
+  __TEXT.__objc_methtype: 0x14d3
+  __TEXT.__objc_stubs: 0x5da0
+  __DATA_CONST.__got: 0x568
+  __DATA_CONST.__const: 0xfb8
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d40
-  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_selrefs: 0x1c58
+  __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x698
-  __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x1160
-  __AUTH_CONST.__objc_const: 0x55f0
+  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0xf80
+  __AUTH_CONST.__objc_const: 0x4bd0
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x5d0
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x4f4
   __DATA.__data: 0x660
-  __DATA.__bss: 0x88
-  __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__bss: 0x50
+  __DATA.__bss: 0xc0
+  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 62CC2F9E-8AAB-372F-990A-3C19F3FB4D39
-  Functions: 926
-  Symbols:   3913
-  CStrings:  2061
+  UUID: 1A54B544-2107-3BFA-9717-444BD1F77DAA
+  Functions: 849
+  Symbols:   3625
+  CStrings:  1933
 
Symbols:
+ +[PKAuthenticator consumeSharedRootContextWithCompletion:]
+ -[PKAuthenticatorSharedRootContext _consumeWithCompletion:reset:]
+ -[PKAuthenticatorSharedRootContext consumeWithCompletion:]
+ GCC_except_table105
+ GCC_except_table179
+ GCC_except_table187
+ GCC_except_table191
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table57
+ GCC_except_table69
+ GCC_except_table90
+ GCC_except_table91
+ GCC_except_table97
+ _PKColorForFKCategory
+ _PKIconForApplicationIdentifier
+ _PKIconForFKCategory
+ _PKIconForFKManuallyExcluded
+ _PKIconForSystemImageName
+ ___41+[PKAuthenticator currentStateForPolicy:]_block_invoke.492
+ ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.247
+ ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.248
+ ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.249
+ ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.250
+ ___57-[PKCategoryVisualizationCardView renderLoop:drawAtTime:]_block_invoke.49
+ ___65-[PKAuthenticatorSharedRootContext _consumeWithCompletion:reset:]_block_invoke
+ ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke.256
+ ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke_2.257
+ ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke_3.258
+ ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke_4.261
+ ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke.271
+ ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke_2.272
+ ___block_literal_global.270
+ ___block_literal_global.274
+ ___block_literal_global.330
+ ___block_literal_global.332
+ ___block_literal_global.599
+ ___block_literal_global.614
+ _objc_msgSend$_consumeWithCompletion:reset:
+ _objc_msgSend$alignmentRectInsets
+ _objc_msgSend$bundleRecordWithApplicationIdentifier:error:
+ _objc_msgSend$consumeWithCompletion:
+ _objc_msgSend$imageWithAlignmentRectInsets:
- -[PKPayLaterCardRenderer .cxx_destruct]
- -[PKPayLaterCardRenderer _addInstances:category:time:]
- -[PKPayLaterCardRenderer _countOfActiveInstancesAtTime:]
- -[PKPayLaterCardRenderer _countOfNonExplodingInstances]
- -[PKPayLaterCardRenderer _initWithRenderLoop:overlayLoader:]
- -[PKPayLaterCardRenderer _removeInstances:category:time:]
- -[PKPayLaterCardRenderer _removeInstances:category:time:].cold.1
- -[PKPayLaterCardRenderer _updateRenderPassDescriptorWithDrawable:]
- -[PKPayLaterCardRenderer _updateUniformsForDevice:]
- -[PKPayLaterCardRenderer dealloc]
- -[PKPayLaterCardRenderer initWithRenderLoop:overlay:]
- -[PKPayLaterCardRenderer init]
- -[PKPayLaterCardRenderer invalidate]
- -[PKPayLaterCardRenderer isInvalidated]
- -[PKPayLaterCardRenderer isPresented]
- -[PKPayLaterCardRenderer renderAtTime:]
- -[PKPayLaterCardRenderer rotation]
- -[PKPayLaterCardRenderer setGravity:]
- -[PKPayLaterCardRenderer setMagnitudes:]
- -[PKPayLaterCardRenderer setMagnitudes:].cold.1
- -[PKPayLaterCardRenderer setPresented:]
- -[PKPayLaterCardRenderer setRotation:]
- -[PKPayLaterCardRendererInstance addForces:]
- -[PKPayLaterCardRendererInstance angle]
- -[PKPayLaterCardRendererInstance angularyVelocity]
- -[PKPayLaterCardRendererInstance applyForces]
- -[PKPayLaterCardRendererInstance axis]
- -[PKPayLaterCardRendererInstance category]
- -[PKPayLaterCardRendererInstance explodeAtTime:]
- -[PKPayLaterCardRendererInstance explodeTime]
- -[PKPayLaterCardRendererInstance forces]
- -[PKPayLaterCardRendererInstance initWithPosition:scale:category:]
- -[PKPayLaterCardRendererInstance isIgnoredAtTime:]
- -[PKPayLaterCardRendererInstance mass]
- -[PKPayLaterCardRendererInstance position]
- -[PKPayLaterCardRendererInstance scale]
- -[PKPayLaterCardRendererInstance setPosition:andVelocity:]
- -[PKPayLaterCardRendererInstance size]
- -[PKPayLaterCardRendererInstance smoothedPosition]
- -[PKPayLaterCardRendererInstance uniformWithSkew:now:waveAmplitude:]
- -[PKPayLaterCardRendererInstance velocity]
- -[PKPayLaterCardView .cxx_destruct]
- -[PKPayLaterCardView _initWithOverlay:magnitudesProvider:]
- -[PKPayLaterCardView _setDeviceAttitude:]
- -[PKPayLaterCardView _updateDrawableSize]
- -[PKPayLaterCardView _updateMotionEnabled]
- -[PKPayLaterCardView _updatePaused]
- -[PKPayLaterCardView dealloc]
- -[PKPayLaterCardView didMoveToWindow]
- -[PKPayLaterCardView initWithCoder:]
- -[PKPayLaterCardView initWithFrame:]
- -[PKPayLaterCardView initWithOverlay:magnitudesProvider:]
- -[PKPayLaterCardView init]
- -[PKPayLaterCardView invalidate]
- -[PKPayLaterCardView isInvalidated]
- -[PKPayLaterCardView isMotionEnabled]
- -[PKPayLaterCardView isPaused]
- -[PKPayLaterCardView isPresented]
- -[PKPayLaterCardView layoutSubviews]
- -[PKPayLaterCardView motionManager:didReceiveMotion:]
- -[PKPayLaterCardView refreshMagnitudes]
- -[PKPayLaterCardView renderLoop:didChangeRunnable:]
- -[PKPayLaterCardView renderLoop:drawAtTime:]
- -[PKPayLaterCardView renderLoop:drawableSizeDidChange:]
- -[PKPayLaterCardView setMotionEnabled:]
- -[PKPayLaterCardView setPaused:]
- -[PKPayLaterCardView setPresented:]
- GCC_except_table103
- GCC_except_table176
- GCC_except_table184
- GCC_except_table188
- GCC_except_table196
- GCC_except_table198
- GCC_except_table4
- GCC_except_table55
- GCC_except_table65
- GCC_except_table88
- GCC_except_table89
- GCC_except_table95
- _CGColorCreateCopyByMatchingToColorSpace
- _CGColorGetComponents
- _CGColorGetNumberOfComponents
- _OBJC_CLASS_$_PKColor
- _OBJC_CLASS_$_PKPayLaterCardRenderer
- _OBJC_CLASS_$_PKPayLaterCardRendererInstance
- _OBJC_CLASS_$_PKPayLaterCardView
- _OBJC_IVAR_$_PKPayLaterCardRenderer._backgroundPipelineState
- _OBJC_IVAR_$_PKPayLaterCardRenderer._commandQueue
- _OBJC_IVAR_$_PKPayLaterCardRenderer._drawableHeight
- _OBJC_IVAR_$_PKPayLaterCardRenderer._drawableWidth
- _OBJC_IVAR_$_PKPayLaterCardRenderer._gravity
- _OBJC_IVAR_$_PKPayLaterCardRenderer._instancePipelineState
- _OBJC_IVAR_$_PKPayLaterCardRenderer._instancePlaneDepthScaleFactor
- _OBJC_IVAR_$_PKPayLaterCardRenderer._instanceUniforms
- _OBJC_IVAR_$_PKPayLaterCardRenderer._instanceVertexCoords
- _OBJC_IVAR_$_PKPayLaterCardRenderer._instances
- _OBJC_IVAR_$_PKPayLaterCardRenderer._invalidated
- _OBJC_IVAR_$_PKPayLaterCardRenderer._loop
- _OBJC_IVAR_$_PKPayLaterCardRenderer._magnitudes
- _OBJC_IVAR_$_PKPayLaterCardRenderer._minSeparationAtInstancePlane
- _OBJC_IVAR_$_PKPayLaterCardRenderer._overlay
- _OBJC_IVAR_$_PKPayLaterCardRenderer._overlayAlpha
- _OBJC_IVAR_$_PKPayLaterCardRenderer._overlayLoader
- _OBJC_IVAR_$_PKPayLaterCardRenderer._overlayPipelineState
- _OBJC_IVAR_$_PKPayLaterCardRenderer._presented
- _OBJC_IVAR_$_PKPayLaterCardRenderer._projectionMatrix
- _OBJC_IVAR_$_PKPayLaterCardRenderer._renderPassDescriptor
- _OBJC_IVAR_$_PKPayLaterCardRenderer._rotation
- _OBJC_IVAR_$_PKPayLaterCardRenderer._smoothedPresentedAmount
- _OBJC_IVAR_$_PKPayLaterCardRenderer._smoothedSpacing
- _OBJC_IVAR_$_PKPayLaterCardRenderer._smoothedViewZoom
- _OBJC_IVAR_$_PKPayLaterCardRenderer._smoothedWaveAmount
- _OBJC_IVAR_$_PKPayLaterCardRenderer._uniform
- _OBJC_IVAR_$_PKPayLaterCardRenderer._vertices
- _OBJC_IVAR_$_PKPayLaterCardRenderer._viewHalfHeightAtInstancePlane
- _OBJC_IVAR_$_PKPayLaterCardRenderer._viewHalfWidthAtInstancePlane
- _OBJC_IVAR_$_PKPayLaterCardRenderer._viewMatrix
- _OBJC_IVAR_$_PKPayLaterCardRendererInstance._angle
- _OBJC_IVAR_$_PKPayLaterCardRendererInstance._angularyVelocity
- _OBJC_IVAR_$_PKPayLaterCardRendererInstance._axis
- _OBJC_IVAR_$_PKPayLaterCardRendererInstance._category
- _OBJC_IVAR_$_PKPayLaterCardRendererInstance._explodeTime
- _OBJC_IVAR_$_PKPayLaterCardRendererInstance._forces
- _OBJC_IVAR_$_PKPayLaterCardRendererInstance._mass
- _OBJC_IVAR_$_PKPayLaterCardRendererInstance._position
- _OBJC_IVAR_$_PKPayLaterCardRendererInstance._scale
- _OBJC_IVAR_$_PKPayLaterCardRendererInstance._size
- _OBJC_IVAR_$_PKPayLaterCardRendererInstance._smoothedPosition
- _OBJC_IVAR_$_PKPayLaterCardRendererInstance._velocity
- _OBJC_IVAR_$_PKPayLaterCardView._draw
- _OBJC_IVAR_$_PKPayLaterCardView._effectiveMotionEnabled
- _OBJC_IVAR_$_PKPayLaterCardView._effectivePaused
- _OBJC_IVAR_$_PKPayLaterCardView._framesToRender
- _OBJC_IVAR_$_PKPayLaterCardView._invalidated
- _OBJC_IVAR_$_PKPayLaterCardView._lastRotation
- _OBJC_IVAR_$_PKPayLaterCardView._magnitudesProvider
- _OBJC_IVAR_$_PKPayLaterCardView._motionEnabled
- _OBJC_IVAR_$_PKPayLaterCardView._paused
- _OBJC_IVAR_$_PKPayLaterCardView._pendingMagnitudes
- _OBJC_IVAR_$_PKPayLaterCardView._renderLoop
- _OBJC_IVAR_$_PKPayLaterCardView._renderer
- _OBJC_METACLASS_$_PKPayLaterCardRenderer
- _OBJC_METACLASS_$_PKPayLaterCardRendererInstance
- _OBJC_METACLASS_$_PKPayLaterCardView
- _PKMakeFloat4FromCGColor
- _PKMapsIconForPayLaterMerchant
- _PKPassFrontFaceContentSize
- _RestingQuaternion
- __OBJC_$_INSTANCE_METHODS_PKPayLaterCardRenderer
- __OBJC_$_INSTANCE_METHODS_PKPayLaterCardRendererInstance
- __OBJC_$_INSTANCE_METHODS_PKPayLaterCardView
- __OBJC_$_INSTANCE_VARIABLES_PKPayLaterCardRenderer
- __OBJC_$_INSTANCE_VARIABLES_PKPayLaterCardRendererInstance
- __OBJC_$_INSTANCE_VARIABLES_PKPayLaterCardView
- __OBJC_$_PROP_LIST_PKPayLaterCardRendererInstance
- __OBJC_$_PROP_LIST_PKPayLaterCardView
- __OBJC_CLASS_PROTOCOLS_$_PKPayLaterCardView
- __OBJC_CLASS_RO_$_PKPayLaterCardRenderer
- __OBJC_CLASS_RO_$_PKPayLaterCardRendererInstance
- __OBJC_CLASS_RO_$_PKPayLaterCardView
- __OBJC_METACLASS_RO_$_PKPayLaterCardRenderer
- __OBJC_METACLASS_RO_$_PKPayLaterCardRendererInstance
- __OBJC_METACLASS_RO_$_PKPayLaterCardView
- ___39-[PKPayLaterCardRenderer renderAtTime:]_block_invoke
- ___41+[PKAuthenticator currentStateForPolicy:]_block_invoke.486
- ___48-[PKPayLaterCardRenderer _sortInstancesByZOrder]_block_invoke
- ___53-[PKPayLaterCardRenderer _sortInstancesByExplodeTime]_block_invoke
- ___55-[PKPayLaterCardRenderer _countOfNonExplodingInstances]_block_invoke
- ___56-[PKAuthenticatorSharedRootContext resetWithCompletion:]_block_invoke
- ___56-[PKPayLaterCardRenderer _countOfActiveInstancesAtTime:]_block_invoke
- ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.241
- ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.242
- ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.243
- ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.244
- ___57-[PKCategoryVisualizationCardView renderLoop:drawAtTime:]_block_invoke.46
- ___57-[PKPayLaterCardRenderer _removeInstances:category:time:]_block_invoke
- ___57-[PKPayLaterCardRenderer _removeInstances:category:time:]_block_invoke_2
- ___57-[PKPayLaterCardRenderer _removeInstances:category:time:]_block_invoke_3
- ___57-[PKPayLaterCardRenderer _removeInstances:category:time:]_block_invoke_4
- ___58-[PKPayLaterCardView _initWithOverlay:magnitudesProvider:]_block_invoke
- ___58-[PKPayLaterCardView _initWithOverlay:magnitudesProvider:]_block_invoke_2
- ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke.250
- ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke_2.251
- ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke_3.252
- ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke_4.255
- ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke.265
- ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke_2.266
- ___block_descriptor_32_e40_B16?0"PKPayLaterCardRendererInstance"8l
- ___block_descriptor_32_e47_B32?0"PKPayLaterCardRendererInstance"8Q16^B24l
- ___block_descriptor_32_e75_q24?0"PKPayLaterCardRendererInstance"8"PKPayLaterCardRendererInstance"16l
- ___block_descriptor_40_e47_B32?0"PKPayLaterCardRendererInstance"8Q16^B24l
- ___block_descriptor_40_e8_32w_e34_v16?0"PKPayLaterCardMagnitudes"8lw32l8
- ___block_descriptor_48_e8_32r_e47_v32?0"PKPayLaterCardRendererInstance"8Q16^B24lr32l8
- ___block_descriptor_56_e8_32r_e47_B32?0"PKPayLaterCardRendererInstance"8Q16^B24lr32l8
- ___block_literal_global.142
- ___block_literal_global.144
- ___block_literal_global.146
- ___block_literal_global.264
- ___block_literal_global.268
- ___block_literal_global.324
- ___block_literal_global.326
- ___block_literal_global.592
- ___block_literal_global.607
- ___sincos_stret
- _cos
- _log
- _objc_msgSend$addForces:
- _objc_msgSend$applyForces
- _objc_msgSend$colorFromString:
- _objc_msgSend$colorWithR:G:B:A:
- _objc_msgSend$drawAtPoint:
- _objc_msgSend$explodeAtTime:
- _objc_msgSend$explodeTime
- _objc_msgSend$foodAndDrinksCount
- _objc_msgSend$funCount
- _objc_msgSend$healthCount
- _objc_msgSend$initWithPosition:scale:category:
- _objc_msgSend$isIgnoredAtTime:
- _objc_msgSend$isMonitoring
- _objc_msgSend$isPresented
- _objc_msgSend$merchantCategory
- _objc_msgSend$motion
- _objc_msgSend$pk_objectsPassingTest:
- _objc_msgSend$pk_removeObjectsPassingTest:
- _objc_msgSend$read:
- _objc_msgSend$refreshMagnitudes
- _objc_msgSend$servicesCount
- _objc_msgSend$setPosition:andVelocity:
- _objc_msgSend$setUpdateHandler:
- _objc_msgSend$shoppingCount
- _objc_msgSend$systemBlackColor
- _objc_msgSend$transportcount
- _objc_msgSend$travelCount
- _objc_msgSend$uniformWithSkew:now:waveAmplitude:
- _objc_msgSend$unknownCount
- _objc_msgSend$velocity
- _pow
CStrings:
+ "_consumeWithCompletion:reset:"
+ "alignmentRectInsets"
+ "arrow.left.arrow.right"
+ "arrow.uturn.backward"
+ "banknote"
+ "bolt.house.fill"
+ "bundleRecordWithApplicationIdentifier:error:"
+ "consumeSharedRootContextWithCompletion:"
+ "consumeWithCompletion:"
+ "imageWithAlignmentRectInsets:"
+ "slash.circle"
- "#00c5de"
- "#07ba27"
- "#3a7fff"
- "#41e0c1"
- "#5b66ff"
- "#ae65f9"
- "#e66dd7"
- "#f8ad00"
- "#f99540"
- "#fcff4b"
- "#fe5d35"
- "#ff2400"
- "#ff5e5a"
- "#ff7077"
- "@\"<PKPayLaterCardMagnitudesProvider>\""
- "@\"PKPayLaterCardMagnitudes\""
- "@\"PKPayLaterCardRenderer\""
- "@32@0:8^{CGImage=}16@24"
- "@48@0:816d32q40"
- "B16@?0@\"PKPayLaterCardRendererInstance\"8"
- "B24@0:8d16"
- "B32@?0@\"PKPayLaterCardRendererInstance\"8Q16^B24"
- "D"
- "PKPayLaterCardRenderer"
- "PKPayLaterCardRenderer: could not load metal library - %@."
- "PKPayLaterCardRenderer: could not load overlay texture."
- "PKPayLaterCardRendererInstance"
- "PKPayLaterCardView"
- "PayLater-CardView"
- "T,R,N,V_axis"
- "T,R,N,V_forces"
- "T,R,N,V_position"
- "T,R,N,V_smoothedPosition"
- "T,R,N,V_velocity"
- "TB,N,GisPresented"
- "Td,R,N,V_angle"
- "Td,R,N,V_angularyVelocity"
- "Td,R,N,V_explodeTime"
- "Td,R,N,V_mass"
- "Td,R,N,V_scale"
- "Td,R,N,V_size"
- "Tq,R,N,V_category"
- "_angle"
- "_angularyVelocity"
- "_axis"
- "_backgroundPipelineState"
- "_category"
- "_explodeTime"
- "_forces"
- "_framesToRender"
- "_gravity"
- "_instancePipelineState"
- "_instancePlaneDepthScaleFactor"
- "_instanceUniforms"
- "_instanceVertexCoords"
- "_instances"
- "_magnitudesProvider"
- "_mass"
- "_minSeparationAtInstancePlane"
- "_overlay"
- "_overlayAlpha"
- "_overlayLoader"
- "_pendingMagnitudes"
- "_position"
- "_presented"
- "_projectionMatrix"
- "_scale"
- "_size"
- "_smoothedPosition"
- "_smoothedPresentedAmount"
- "_smoothedSpacing"
- "_smoothedViewZoom"
- "_smoothedWaveAmount"
- "_velocity"
- "_viewHalfHeightAtInstancePlane"
- "_viewHalfWidthAtInstancePlane"
- "_viewMatrix"
- "addForces:"
- "angle"
- "angularyVelocity"
- "applyForces"
- "axis"
- "colorFromString:"
- "colorWithR:G:B:A:"
- "drawAtPoint:"
- "explodeAtTime:"
- "explodeTime"
- "foodAndDrinksCount"
- "forces"
- "funCount"
- "healthCount"
- "initWithOverlay:magnitudesProvider:"
- "initWithPosition:scale:category:"
- "isIgnoredAtTime:"
- "isPresented"
- "mass"
- "merchantCategory"
- "payLaterCard_fragment_background"
- "payLaterCard_fragment_instances"
- "payLaterCard_fragment_overlay"
- "payLaterCard_instanceVertex"
- "payLaterCard_vertex"
- "pk_objectsPassingTest:"
- "pk_removeObjectsPassingTest:"
- "presented"
- "q24@?0@\"PKPayLaterCardRendererInstance\"8@\"PKPayLaterCardRendererInstance\"16"
- "refreshMagnitudes"
- "servicesCount"
- "setPosition:andVelocity:"
- "setPresented:"
- "setUpdateHandler:"
- "shoppingCount"
- "smoothedPosition"
- "systemBlackColor"
- "transportcount"
- "travelCount"
- "uniformWithSkew:now:waveAmplitude:"
- "unknownCount"
- "v16@?0@\"PKPayLaterCardMagnitudes\"8"
- "v32@0:816"
- "v32@?0@\"PKPayLaterCardRendererInstance\"8Q16^B24"
- "v48@0:81632"
- "velocity"
- "{PayLaterInstanceUniform={?=[4]}}40@0:816d24d32"

```
