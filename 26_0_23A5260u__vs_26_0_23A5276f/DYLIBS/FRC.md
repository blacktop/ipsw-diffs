## FRC

> `/System/Library/PrivateFrameworks/FRC.framework/FRC`

```diff

-226.0.0.0.0
-  __TEXT.__text: 0x2e4d4
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x2b2c
-  __TEXT.__const: 0x550
-  __TEXT.__cstring: 0x4a3b
-  __TEXT.__oslogstring: 0x45e
+228.0.0.0.0
+  __TEXT.__text: 0x312ec
+  __TEXT.__auth_stubs: 0xe30
+  __TEXT.__objc_methlist: 0x2da4
+  __TEXT.__const: 0x560
+  __TEXT.__cstring: 0x54de
+  __TEXT.__oslogstring: 0x76e
   __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0x8e0
-  __TEXT.__objc_classname: 0x323
-  __TEXT.__objc_methname: 0xa90a
-  __TEXT.__objc_methtype: 0x31d9
-  __TEXT.__objc_stubs: 0x5180
-  __DATA_CONST.__got: 0x3f8
+  __TEXT.__unwind_info: 0x960
+  __TEXT.__objc_classname: 0x337
+  __TEXT.__objc_methname: 0xb11d
+  __TEXT.__objc_methtype: 0x3471
+  __TEXT.__objc_stubs: 0x55c0
+  __DATA_CONST.__got: 0x400
   __DATA_CONST.__const: 0x508
-  __DATA_CONST.__objc_classlist: 0x130
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ab0
-  __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__auth_got: 0x590
-  __AUTH_CONST.__const: 0xb8
-  __AUTH_CONST.__cfstring: 0x30c0
-  __AUTH_CONST.__objc_const: 0x7a70
-  __DATA.__objc_ivar: 0x988
+  __DATA_CONST.__objc_selrefs: 0x1c28
+  __DATA_CONST.__objc_superrefs: 0x100
+  __AUTH_CONST.__auth_got: 0x728
+  __AUTH_CONST.__const: 0xd8
+  __AUTH_CONST.__cfstring: 0x3200
+  __AUTH_CONST.__objc_const: 0x80e0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xa28
   __DATA.__data: 0x140
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9CFB5D51-B8F1-3D02-A650-67B44FE373B4
-  Functions: 994
-  Symbols:   3791
-  CStrings:  2847
+  UUID: DB2B0F79-FE93-33E0-9B02-524BEC441823
+  Functions: 1063
+  Symbols:   4061
+  CStrings:  3036
 
Symbols:
+ -[FRCFrameInterpolator bypassNormalizationForOpticalFlowInput]
+ -[FRCFrameInterpolator e5OpticalFlowModel]
+ -[FRCFrameInterpolator setBypassNormalizationForOpticalFlowInput:]
+ -[FRCFrameInterpolator setE5OpticalFlowModel:]
+ -[FRCOpticalFlowEstimatorConfiguration .cxx_destruct]
+ -[FRCOpticalFlowEstimatorConfiguration bypassInputNormalization]
+ -[FRCOpticalFlowEstimatorConfiguration e5Model]
+ -[FRCOpticalFlowEstimatorConfiguration setBypassInputNormalization:]
+ -[FRCOpticalFlowEstimatorConfiguration setE5Model:]
+ -[FRCOpticalFlowEstimatorConfiguration setUseE5RT:]
+ -[FRCOpticalFlowEstimatorConfiguration useE5RT]
+ -[OpticalFlow bypassInputNormalization]
+ -[OpticalFlow originalFirst]
+ -[OpticalFlow originalSecond]
+ -[OpticalFlow reshuffleFlow:previsouFlow:destination:waitForComplete:]
+ -[OpticalFlow resourcePreAllocated]
+ -[OpticalFlow setBypassInputNormalization:]
+ -[OpticalFlow setNumLevels:]
+ -[OpticalFlow setOriginalFirst:]
+ -[OpticalFlow setOriginalSecond:]
+ -[OpticalFlow setResourcePreAllocated:]
+ -[OpticalFlow upscaleFinalFlow]
+ -[OpticalFlowE5 .cxx_destruct]
+ -[OpticalFlowE5 allocateBufferObjects]
+ -[OpticalFlowE5 bindPorts]
+ -[OpticalFlowE5 buildLibraryForModel:]
+ -[OpticalFlowE5 buildLibraryForModel:].cold.1
+ -[OpticalFlowE5 buildLibraryFromE5BundleForModel:]
+ -[OpticalFlowE5 buildLibraryFromE5BundleForModel:].cold.1
+ -[OpticalFlowE5 checkDefaults]
+ -[OpticalFlowE5 checkInputResolutions]
+ -[OpticalFlowE5 createFP16TextureFromIOSurface:width:height:channels:]
+ -[OpticalFlowE5 dealloc]
+ -[OpticalFlowE5 encodeConvertLinearBuffer:toPixelBuffer:]
+ -[OpticalFlowE5 encodeCovnertPixelBuffer:toLinearBuffer:toCommandBuffer:]
+ -[OpticalFlowE5 executeModel]
+ -[OpticalFlowE5 executeModel].cold.1
+ -[OpticalFlowE5 firstFrameSurface]
+ -[OpticalFlowE5 getPortNames]
+ -[OpticalFlowE5 initWithMode:]
+ -[OpticalFlowE5 initWithModel:usage:]
+ -[OpticalFlowE5 initWithModel:usage:].cold.1
+ -[OpticalFlowE5 initWithModel:usage:].cold.2
+ -[OpticalFlowE5 initWithModel:usage:].cold.3
+ -[OpticalFlowE5 initWithModel:usage:].cold.4
+ -[OpticalFlowE5 initializeModel:]
+ -[OpticalFlowE5 initializeModel:].cold.1
+ -[OpticalFlowE5 opticalFlowFirstFrame:secondFrame:flow:]
+ -[OpticalFlowE5 opticalFlowFirstFrame:secondFrame:flowForward:flowBackward:reUseFlow:]
+ -[OpticalFlowE5 outputSurface]
+ -[OpticalFlowE5 releaseAdaptationLayerStorage]
+ -[OpticalFlowE5 releaseBufferObjects]
+ -[OpticalFlowE5 resetStream:]
+ -[OpticalFlowE5 secondFrameSurface]
+ -[OpticalFlowE5 setFirstFrameSurface:]
+ -[OpticalFlowE5 setOutputSurface:]
+ -[OpticalFlowE5 setSecondFrameSurface:]
+ -[OpticalFlowE5 setupAdaptationLayer]
+ -[OpticalFlowE5 subsampleAndNormalizeInput:to:]
+ -[OpticalFlowE5 switchUsageTo:]
+ -[OpticalFlowE5 switchUsageTo:].cold.1
+ -[OpticalFlowE5 upscaleFlowWithFlowAdaptationLayerFirstFrame:secondFrame:baseFlow:destination:]
+ GCC_except_table26
+ OBJC_IVAR_$_OpticalFlow._commandQueue
+ OBJC_IVAR_$_OpticalFlow._usage
+ _FRCGetUsageFromSizeE5
+ _IOSurfaceGetPixelFormat
+ _OBJC_CLASS_$_OpticalFlowE5
+ _OBJC_IVAR_$_FRCFrameInterpolator._bypassNormalizationForOpticalFlowInput
+ _OBJC_IVAR_$_FRCFrameInterpolator._e5OpticalFlowModel
+ _OBJC_IVAR_$_FRCOpticalFlowEstimator._bypassInputNormalization
+ _OBJC_IVAR_$_FRCOpticalFlowEstimator._useE5RT
+ _OBJC_IVAR_$_FRCOpticalFlowEstimatorConfiguration._bypassInputNormalization
+ _OBJC_IVAR_$_FRCOpticalFlowEstimatorConfiguration._e5Model
+ _OBJC_IVAR_$_FRCOpticalFlowEstimatorConfiguration._useE5RT
+ _OBJC_IVAR_$_OpticalFlow._bypassInputNormalization
+ _OBJC_IVAR_$_OpticalFlow._originalFirst
+ _OBJC_IVAR_$_OpticalFlow._originalSecond
+ _OBJC_IVAR_$_OpticalFlowE5._backwarp
+ _OBJC_IVAR_$_OpticalFlowE5._deviceType
+ _OBJC_IVAR_$_OpticalFlowE5._features
+ _OBJC_IVAR_$_OpticalFlowE5._fidelityWeightBufferObject
+ _OBJC_IVAR_$_OpticalFlowE5._firstFrameSurface
+ _OBJC_IVAR_$_OpticalFlowE5._function
+ _OBJC_IVAR_$_OpticalFlowE5._inputBufferObject
+ _OBJC_IVAR_$_OpticalFlowE5._inputPortNames
+ _OBJC_IVAR_$_OpticalFlowE5._inputSize
+ _OBJC_IVAR_$_OpticalFlowE5._input_ports
+ _OBJC_IVAR_$_OpticalFlowE5._intermediateFlow
+ _OBJC_IVAR_$_OpticalFlowE5._library
+ _OBJC_IVAR_$_OpticalFlowE5._logger
+ _OBJC_IVAR_$_OpticalFlowE5._normalization
+ _OBJC_IVAR_$_OpticalFlowE5._num_input_ports
+ _OBJC_IVAR_$_OpticalFlowE5._operation
+ _OBJC_IVAR_$_OpticalFlowE5._opticalFlowStorage
+ _OBJC_IVAR_$_OpticalFlowE5._outputBufferObject
+ _OBJC_IVAR_$_OpticalFlowE5._outputPortName
+ _OBJC_IVAR_$_OpticalFlowE5._outputSize
+ _OBJC_IVAR_$_OpticalFlowE5._outputSurface
+ _OBJC_IVAR_$_OpticalFlowE5._output_port
+ _OBJC_IVAR_$_OpticalFlowE5._scaler
+ _OBJC_IVAR_$_OpticalFlowE5._secondFrameSurface
+ _OBJC_IVAR_$_OpticalFlowE5._stream
+ _OBJC_IVAR_$_OpticalFlowE5._subsampledBGRA
+ _OBJC_IVAR_$_OpticalFlowE5._subsampledFirst
+ _OBJC_IVAR_$_OpticalFlowE5._subsampledOriginalFirst
+ _OBJC_IVAR_$_OpticalFlowE5._subsampledOriginalSecond
+ _OBJC_IVAR_$_OpticalFlowE5._subsampledSecond
+ _OBJC_METACLASS_$_OpticalFlowE5
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _TensorSizeMake
+ __OBJC_$_INSTANCE_METHODS_OpticalFlowE5
+ __OBJC_$_INSTANCE_VARIABLES_OpticalFlowE5
+ __OBJC_$_PROP_LIST_OpticalFlowE5
+ __OBJC_CLASS_RO_$_OpticalFlowE5
+ __OBJC_METACLASS_RO_$_OpticalFlowE5
+ ___115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.105
+ ___115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke_2.106
+ ___createLogger_block_invoke
+ _createLogger.logger
+ _createLogger.onceToken
+ _dispatch_once
+ _e5rt_async_event_create
+ _e5rt_async_event_release
+ _e5rt_buffer_object_get_iosurface
+ _e5rt_buffer_object_release
+ _e5rt_e5_compiler_compile
+ _e5rt_e5_compiler_create
+ _e5rt_e5_compiler_options_create
+ _e5rt_e5_compiler_options_release
+ _e5rt_e5_compiler_options_set_compute_device_types_mask
+ _e5rt_e5_compiler_release
+ _e5rt_execution_stream_create
+ _e5rt_execution_stream_encode_operation
+ _e5rt_execution_stream_execute_sync
+ _e5rt_execution_stream_operation_bind_completion_event
+ _e5rt_execution_stream_operation_bind_dependent_events
+ _e5rt_execution_stream_operation_create_precompiled_compute_operation_with_options
+ _e5rt_execution_stream_operation_get_input_names
+ _e5rt_execution_stream_operation_get_num_inputs
+ _e5rt_execution_stream_operation_get_num_outputs
+ _e5rt_execution_stream_operation_get_output_names
+ _e5rt_execution_stream_operation_prepare_op_for_encode
+ _e5rt_execution_stream_operation_release
+ _e5rt_execution_stream_operation_retain_input_port
+ _e5rt_execution_stream_operation_retain_output_port
+ _e5rt_execution_stream_release
+ _e5rt_execution_stream_reset
+ _e5rt_get_last_error_message
+ _e5rt_io_port_bind_buffer_object
+ _e5rt_io_port_is_tensor
+ _e5rt_io_port_release
+ _e5rt_io_port_retain_surface_desc
+ _e5rt_io_port_retain_tensor_desc
+ _e5rt_precompiled_compute_op_create_options_create_with_program_function
+ _e5rt_precompiled_compute_op_create_options_release
+ _e5rt_program_function_release
+ _e5rt_program_library_create
+ _e5rt_program_library_release
+ _e5rt_program_library_retain_program_function
+ _e5rt_surface_desc_get_format
+ _e5rt_surface_desc_get_height
+ _e5rt_surface_desc_get_width
+ _e5rt_tensor_desc_alloc_buffer_object
+ _e5rt_tensor_desc_dtype_get_element_size
+ _e5rt_tensor_desc_dtype_release
+ _e5rt_tensor_desc_get_shape
+ _e5rt_tensor_desc_get_strides
+ _e5rt_tensor_desc_release
+ _e5rt_tensor_desc_retain_dtype
+ _exit
+ _getInternalBundle
+ _getPortShape
+ _getPortShape.cold.1
+ _objc_msgSend$allocateBufferObjects
+ _objc_msgSend$bindPorts
+ _objc_msgSend$buildLibraryForModel:
+ _objc_msgSend$buildLibraryFromE5BundleForModel:
+ _objc_msgSend$bundlePath
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$bypassInputNormalization
+ _objc_msgSend$checkDefaults
+ _objc_msgSend$checkInputResolutions
+ _objc_msgSend$createFP16TextureFromIOSurface:width:height:channels:
+ _objc_msgSend$e5Model
+ _objc_msgSend$encodeConvertLinearBuffer:toPixelBuffer:
+ _objc_msgSend$encodeCovnertPixelBuffer:toLinearBuffer:toCommandBuffer:
+ _objc_msgSend$executeModel
+ _objc_msgSend$getPortNames
+ _objc_msgSend$initWithModel:usage:
+ _objc_msgSend$initializeModel:
+ _objc_msgSend$originalFirst
+ _objc_msgSend$originalSecond
+ _objc_msgSend$releaseAdaptationLayerStorage
+ _objc_msgSend$releaseBufferObjects
+ _objc_msgSend$resetStream:
+ _objc_msgSend$reshuffleFlow:previsouFlow:destination:waitForComplete:
+ _objc_msgSend$setBypassInputNormalization:
+ _objc_msgSend$setOriginalFirst:
+ _objc_msgSend$setOriginalSecond:
+ _objc_msgSend$setResourcePreAllocated:
+ _objc_msgSend$setupAdaptationLayer
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$subsampleAndNormalizeInput:to:
+ _objc_msgSend$upscaleFinalFlow
+ _objc_msgSend$upscaleFlowWithFlowAdaptationLayerFirstFrame:secondFrame:baseFlow:destination:
+ _objc_msgSend$useE5RT
- -[OpticalFlow reshuffleFlow:previsouFlow:destination:]
- GCC_except_table25
- _OBJC_IVAR_$_OpticalFlow._commandQueue
- _OBJC_IVAR_$_OpticalFlow._usage
- ___115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.104
- ___115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke_2.105
- _objc_msgSend$reshuffleFlow:previsouFlow:destination:
CStrings:
+ "@48@0:8^{__IOSurface=}16q24q32q40"
+ "AppleInternal"
+ "Creating library from pre-built bundle at %@"
+ "E5RTDevice"
+ "ERROR!: Failed to compile model %@"
+ "ERROR!: Failed to create library from bundle %@\n"
+ "Error invalid number of input ports (%ld)\n"
+ "Error! Model input resolution does not match with usage (Model expects %ld x %ld, Usage: %ld x %ld"
+ "Excecution failed. returned error = %u. msg = %s\n"
+ "FAILURE: \"%s\" returned error = %u. msg = %s\n"
+ "Failed to build model"
+ "Failed to create normalization"
+ "Failed to create scaler"
+ "GPU"
+ "Input image [%@]: %ld x %ld x %ld"
+ "Number of Input Ports = %ld"
+ "OpticalFlowE5"
+ "Output Flow [%@]: %ld x %ld x %ld"
+ "PWCNet_540p_lv2Flow_9x9corrANE"
+ "Pre-compiled E5 Bundle for %@ is not availble. Switching to runtime compilation."
+ "Runtime Compilation\n"
+ "System"
+ "T@\"NSString\",&,N,V_e5Model"
+ "T@\"NSString\",&,N,V_e5OpticalFlowModel"
+ "TB,N,V_bypassInputNormalization"
+ "TB,N,V_bypassNormalizationForOpticalFlowInput"
+ "TB,N,V_resourcePreAllocated"
+ "TB,N,V_useE5RT"
+ "TB,R,V_upscaleFinalFlow"
+ "T^{__CVBuffer=},N,V_originalFirst"
+ "T^{__CVBuffer=},N,V_originalSecond"
+ "T^{__IOSurface=},N,V_firstFrameSurface"
+ "T^{__IOSurface=},N,V_outputSurface"
+ "T^{__IOSurface=},N,V_secondFrameSurface"
+ "Ti,N,V_numLevels"
+ "Unsupported Resolution"
+ "[2^{e5rt_buffer_object}]"
+ "[2^{e5rt_io_port}]"
+ "[OpticalFlowE5] Error! Tensor dtype is %ld bits. Must be fp16"
+ "[OpticalFlowE5] Port is a surface type"
+ "[OpticalFlowE5] Port is a tensor type"
+ "[OpticalFlowE5] failed to get surface format"
+ "^{__IOSurface=}"
+ "^{__IOSurface=}16@0:8"
+ "^{e5rt_buffer_object=}"
+ "^{e5rt_execution_stream=}"
+ "^{e5rt_execution_stream_operation=}"
+ "^{e5rt_io_port=}"
+ "^{e5rt_program_function=}"
+ "^{e5rt_program_library=}"
+ "_bypassInputNormalization"
+ "_bypassNormalizationForOpticalFlowInput"
+ "_deviceType"
+ "_e5Model"
+ "_e5OpticalFlowModel"
+ "_fidelityWeightBufferObject"
+ "_firstFrameSurface"
+ "_function"
+ "_inputBufferObject"
+ "_inputPortNames"
+ "_inputSize"
+ "_input_ports"
+ "_library"
+ "_num_input_ports"
+ "_operation"
+ "_opticalFlowStorage"
+ "_originalFirst"
+ "_originalSecond"
+ "_outputBufferObject"
+ "_outputPortName"
+ "_outputSize"
+ "_outputSurface"
+ "_output_port"
+ "_secondFrameSurface"
+ "_stream"
+ "_subsampledBGRA"
+ "_subsampledFirst"
+ "_subsampledOriginalFirst"
+ "_subsampledOriginalSecond"
+ "_subsampledSecond"
+ "_useE5RT"
+ "allocateBufferObjects"
+ "bindPorts"
+ "buildLibraryForModel:"
+ "buildLibraryFromE5BundleForModel:"
+ "bundle"
+ "bundlePath"
+ "bundleWithPath:"
+ "bypassInputNormalization"
+ "bypassNormalizationForOpticalFlowInput"
+ "checkDefaults"
+ "checkInputResolutions"
+ "completion event"
+ "createFP16TextureFromIOSurface:width:height:channels:"
+ "dependent Event"
+ "e5Bundles"
+ "e5Model"
+ "e5OpticalFlowModel"
+ "e5rt_async_event_create(&completionEvent, \"completion event\", E5RT_ASYNC_EVENT_TYPE_IOSURFACE_SHARED_EVENT)"
+ "e5rt_async_event_create(&dependentEvent, \"dependent Event\", E5RT_ASYNC_EVENT_TYPE_IOSURFACE_SHARED_EVENT)"
+ "e5rt_buffer_object_get_iosurface(_inputBufferObject[0], &_firstFrameSurface)"
+ "e5rt_buffer_object_get_iosurface(_inputBufferObject[1], &_secondFrameSurface)"
+ "e5rt_buffer_object_get_iosurface(_outputBufferObject, &_outputSurface)"
+ "e5rt_e5_compiler_create (&compiler)"
+ "e5rt_e5_compiler_options_create(&options)"
+ "e5rt_e5_compiler_options_set_compute_device_types_mask(options, deviceMask)"
+ "e5rt_execution_stream_create(&_stream)"
+ "e5rt_execution_stream_encode_operation(_stream, _operation)"
+ "e5rt_execution_stream_operation_bind_completion_event(_operation, completionEvent)"
+ "e5rt_execution_stream_operation_bind_dependent_events(_operation, &dependentEvent, 1)"
+ "e5rt_execution_stream_operation_create_precompiled_compute_operation_with_options(&_operation, create_options)"
+ "e5rt_execution_stream_operation_prepare_op_for_encode(_operation)"
+ "e5rt_execution_stream_operation_retain_input_port(_operation, _inputPortNames[inputIdx].UTF8String, &_input_ports[inputIdx])"
+ "e5rt_execution_stream_operation_retain_output_port(_operation, _outputPortName.UTF8String, &_output_port)"
+ "e5rt_execution_stream_reset(stream)"
+ "e5rt_io_port_bind_buffer_object(_input_ports[i], _inputBufferObject[i])"
+ "e5rt_io_port_bind_buffer_object(_output_port, _outputBufferObject)"
+ "e5rt_io_port_is_tensor(port, &is_tensor)"
+ "e5rt_io_port_retain_surface_desc(port, &surface_desc)"
+ "e5rt_io_port_retain_tensor_desc(_input_ports[inputIdx], &input_tensor_desc)"
+ "e5rt_io_port_retain_tensor_desc(_output_port, &output_tensor_desc)"
+ "e5rt_io_port_retain_tensor_desc(port, &tensor_desc)"
+ "e5rt_precompiled_compute_op_create_options_create_with_program_function(&create_options, _function)"
+ "e5rt_program_library_retain_program_function(_library, \"main\", &_function)"
+ "e5rt_surface_desc_get_height(surface_desc, height)"
+ "e5rt_surface_desc_get_width(surface_desc, width)"
+ "e5rt_tensor_desc_alloc_buffer_object(input_tensor_desc, E5RT_BUFFER_OBJECT_TYPE_IOSURFACE, 1, &_inputBufferObject[inputIdx])"
+ "e5rt_tensor_desc_alloc_buffer_object(output_tensor_desc, E5RT_BUFFER_OBJECT_TYPE_IOSURFACE, 1, &_outputBufferObject)"
+ "e5rt_tensor_desc_get_shape(tensor_desc, &rank, &shape)"
+ "e5rt_tensor_desc_get_strides(tensor_desc, &rank, &strides)"
+ "e5rt_tensor_desc_retain_dtype(tensor_desc, &tensor_dtype)"
+ "encodeConvertLinearBuffer:toPixelBuffer:"
+ "encodeCovnertPixelBuffer:toLinearBuffer:toCommandBuffer:"
+ "executeModel"
+ "failed to build library"
+ "failed to obtain input info"
+ "firstFrameSurface"
+ "getPortNames"
+ "initWithModel:usage:"
+ "initializeModel:"
+ "landscape1024x768"
+ "main"
+ "mlmodelc"
+ "mlpackage"
+ "model.mil"
+ "originalFirst"
+ "originalSecond"
+ "outputSurface"
+ "releaseAdaptationLayerStorage"
+ "releaseBufferObjects"
+ "resetStream:"
+ "reshuffleFlow:previsouFlow:destination:waitForComplete:"
+ "resourcePreAllocated"
+ "secondFrameSurface"
+ "setBypassInputNormalization:"
+ "setBypassNormalizationForOpticalFlowInput:"
+ "setE5Model:"
+ "setE5OpticalFlowModel:"
+ "setFirstFrameSurface:"
+ "setOriginalFirst:"
+ "setOriginalSecond:"
+ "setOutputSurface:"
+ "setResourcePreAllocated:"
+ "setSecondFrameSurface:"
+ "setUseE5RT:"
+ "setupAdaptationLayer"
+ "stringByAppendingPathComponent:"
+ "stringByDeletingPathExtension"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "subsampleAndNormalizeInput:to:"
+ "upscaleFinalFlow"
+ "upscaleFlowWithFlowAdaptationLayerFirstFrame:secondFrame:baseFlow:destination:"
+ "useE5RT"
+ "v24@0:8^{__IOSurface=}16"
+ "v24@0:8^{e5rt_execution_stream=}16"
+ "v32@0:8^{__IOSurface=}16^{__CVBuffer=}24"
+ "v40@0:8^{__CVBuffer=}16^{__IOSurface=}24@32"
+ "v44@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32B40"
+ "{?=\"correlations\"[6^{__CVBuffer}]\"flows\"[6^{__CVBuffer}]\"upscaledFlows\"[6^{__CVBuffer}]\"warpedImages\"[6^{__CVBuffer}]\"shuffledFlow\"^{__CVBuffer}\"numLevels\"I}"
+ "{?=\"width\"Q\"height\"Q\"channels\"Q}"
- "Ti,R,N,V_numLevels"
- "reshuffleFlow:previsouFlow:destination:"

```
