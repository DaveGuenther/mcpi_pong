# this file is used to define global strings used in multiple parts of the program, such as error notifications

def type_error_message(required_class, found_class):
    err_msg = "Required object of type <class "+str(required_class.__module__)+"."+str(required_class.__name__)+">.  Found object of type "+str(type(found_class))+" instead."
    return err_msg