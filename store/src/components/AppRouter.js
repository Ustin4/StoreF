import {observer} from "mobx-react-lite";
import {useContext} from "react";
import {Navigate, Route, Routes, useNavigate} from "react-router-dom";
import {Context} from "../index";
import {SHOP_ROUTE} from "../utils/consts";
import {authRoutes, publicRoutes} from "../routes";

const AppRouter = observer(() => {
    const {user} = useContext(Context)
    const navigate = useNavigate()
    console.log(user)

    // if (user.isAuth) {
    //     navigate(SHOP_ROUTE);
    // }
    return (
        <Routes>
            {user.isAuth && authRoutes.map(({ path, Component }) =>
                <Route key={path} path={path} component={Component} exact />
            )}

            {publicRoutes.map(({ path, element }) =>
                <Route key={path} path={path} element={element} exact />
            )}

            <Route path="*" element={<Navigate to={SHOP_ROUTE} />} />
            {/*<Redirect to={SHOP_ROUTE}/>*/}
        </Routes>
    );
});

export default AppRouter;
