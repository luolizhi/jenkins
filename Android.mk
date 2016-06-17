################################################################################
# Android hello-world makefile                                           #
################################################################################
LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := teec
LOCAL_SRC_FILES := public/libteec.so
#LOCAL_MODULE_CLASS := SHARED_LIBRARIES
#LOCAL_MODULE_SUFFIX := .so
LOCAL_EXPORT_C_INCLUDES := $(LOCAL_PATH)/public
include $(PREBUILT_SHARED_LIBRARY)


include $(CLEAR_VARS)
  LOCAL_C_INCLUDES := \
      $(LOCAL_PATH)/host \
      $(LOCAL_PATH)/public
      
  LOCAL_SHARED_LIBRARIES := libteec
 
  LOCAL_SRC_FILES := \
      host/*.c

      
 LOCAL_MODULE := helloworld
LOCAL_MODULE_TAGS := optional
include $(BUILD_EXECUTABLE)
