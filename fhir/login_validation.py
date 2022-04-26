from kanpai import Kanpai


schema = Kanpai.Object({
 "useremail"    : (Kanpai.Email(error='User email must be email.')
                  .trim()
                  .required(error='Please provide user email.')
                  .max(20, error='Maximum allowed length is 50')
                  .min(4, 'user name must be minimum 10')),

 "password"    : (Kanpai.String(error='User password must be string.')
                  .trim()
                  .required(error='Please provide user password.')
                  .max(20, error='Maximum allowed length is 20')
                  .min(4, 'user password must be minimum 4')),

})